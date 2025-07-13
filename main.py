from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Fortschrittszustand im Speicher (später DB)
user_progress = {}

# Kurse aus JSON laden
def load_courses():
    with open("data/courses_generated.json", encoding="utf-8") as f:
        data = json.load(f)
        return data["courses"]  # 👈 Achte auf den richtigen Schlüssel


@app.route("/")
def home():
    all_courses = load_courses()
    name = "Thomas"

    # Fortschritt einfügen
    for course in all_courses:
        course_id = course["id"]
        course["progress"] = user_progress.get(course_id, course.get("progress", 0))

    # Angefangene Kurse: alle mit Fortschritt > 0
    ongoing = [c for c in all_courses if c["progress"] > 0]

    # Empfohlene, Community, YouTube nach Kategorie trennen
    empfohlen = [c for c in all_courses if c["type"] == "empfohlen"]
    community = [c for c in all_courses if c["type"] == "community"]
    youtube_courses = [c for c in all_courses if c["type"] == "youtube"]

    # Durchschnittlicher Fortschritt
    avg_progress = int(sum([c["progress"] for c in ongoing]) / len(ongoing)) if ongoing else 0

    return render_template("home.html",
                           name=name,
                           learn_progress=avg_progress,
                           ongoing=ongoing,
                           empfohlen=empfohlen,
                           community=community,
                           youtube_courses=youtube_courses)

@app.route("/kurs/<int:course_id>")
def course_detail(course_id):
    all_courses = load_courses()
    course = next((c for c in all_courses if c["id"] == course_id), None)
    if course:
        return render_template("course_detail.html", course=course)
    return "Kurs nicht gefunden", 404

@app.route("/kurs/<int:course_id>/lernen")
def course_learn(course_id):
    all_courses = load_courses()
    course = next((c for c in all_courses if c["id"] == course_id), None)
    if course:
        progress = user_progress.get(course_id, course.get("progress", 0))
        chapters = course.get("chapters", [
            {"title": "Einführung", "duration": "5:00"},
            {"title": "Hauptteil", "duration": "12:00"},
            {"title": "Zusammenfassung", "duration": "3:00"}
        ])
        return render_template("course_learn.html", course=course, chapters=chapters, progress=progress)
    return "Nicht gefunden", 404

@app.route("/api/progress/<int:course_id>", methods=["POST"])
def update_progress(course_id):
    data = request.get_json()
    progress = data.get("progress")
    if isinstance(progress, int) and 0 <= progress <= 100:
        user_progress[course_id] = progress
        return jsonify(success=True)
    return jsonify(success=False, error="Ungültiger Fortschritt"), 400

@app.route("/suche")
def suche():
    all_courses = load_courses()
    return render_template("course_search.html", courses=all_courses)

@app.route("/api/courses")
def api_courses():
    courses = load_courses()

    # Alle Parameter einsammeln
    query = request.args.get("query", "").strip().lower()
    kategorie = request.args.get("kategorie", "").strip().lower()
    rolle = request.args.get("rolle", "").strip().lower()
    format_ = request.args.get("format", "").strip().lower()
    sprache = request.args.get("sprache", "").strip().lower()
    sort = request.args.get("sort", "").strip().lower()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 6))

    # Filter anwenden
    def match(course):
        return (
            (not query or query in course.get("title", "").lower() or query in course.get("short_description", "").lower()) and
            (not kategorie or kategorie in course.get("category", "").lower()) and
            (not rolle or rolle in course.get("level", "").lower()) and
            (not format_ or format_ in course.get("format", "").lower()) and
            (not sprache or sprache in course.get("language", "").lower())
        )

    filtered = list(filter(match, courses))

    # Sortierung
    if sort == "az":
        filtered.sort(key=lambda c: c.get("title", "").lower())
    elif sort == "dauer_auf":
        filtered.sort(key=lambda c: c.get("duration_minutes", 0))
    elif sort == "dauer_ab":
        filtered.sort(key=lambda c: c.get("duration_minutes", 0), reverse=True)
    elif sort == "neueste":
        filtered.sort(key=lambda c: c.get("created_at", ""), reverse=True)  # optional: Datum als ISO speichern
    # default: keine Sortierung oder Beliebtheit

    # Pagination
    total = len(filtered)
    total_pages = max((total + per_page - 1) // per_page, 1)
    start = (page - 1) * per_page
    end = start + per_page
    paginated = filtered[start:end]

    return jsonify({
        "courses": paginated,
        "page": page,
        "total_pages": total_pages,
        "total": total
    })

@app.route("/api/search")
def live_search():
    query = request.args.get("q", "").lower()
    courses_data = load_courses()
    if not query:
        return jsonify(results=[])

    results = [
        {
            "id": course["id"],
            "title": course["title"],
            "short_description": course.get("short_description", "")
        }
        for course in courses_data
        if query in course["title"].lower() or query in course.get("short_description", "").lower()
    ][:8]  # max 8 Ergebnisse

    return jsonify(results=results)


@app.route("/favoriten")
def favoriten():
    return render_template("favorites.html")

@app.route("/community")
def community():
    return render_template("community.html")

if __name__ == "__main__":
    app.run(debug=True)

# http://localhost:5000/api/courses?query=python&rolle=einsteiger&sort=az&page=1

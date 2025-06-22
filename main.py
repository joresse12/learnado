from flask import Flask, render_template
from data import courses, community, empfohlen, started, youtube_courses

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        {"id": 1, "title": "Einführung in Machine Learning","short_description":"Ein praxisnaher Einstieg in die Grundlagen des maschinellen Lernens inklusive Klassifikation, Regression und Clustering.","owner": "Felix Schneider", "img": "static/images/kurse/machine_learning.jpg"},
        {"id": 2, "title": "Projektmanagement","short_description":"Erfahre die Grundlagen des Projektmanagements von Planung und Organisation bis hin zu Risikomanagement und erfolgreicher Teamführung.", "owner": "Anna Becker","img": "static/images/kurse/project_management_skill.jpg"},
        {"id": 3, "title": "Cybersecurity 1","short_description":"Lerne die wichtigsten Methoden zum Schutz von IT-Systemen und Netzwerken gegen Cyberangriffe","owner": "Jonas Weber", "img": "static/images/kurse/CyberSecurity.png"},
        {"id": 4, "title": "Supply Chain Management","short_description":"Verstehe die Abläufe in Lieferketten und lerne, wie du Effizienz und Nachhaltigkeit steigerst.","owner": "Mira Solvane", "img": "static/images/kurse/SupplyChainManagement.png"},
        {"id": 5, "title":  "Projektcontrolling und Erfolgsmessung","short_description":"Erlerne Techniken zur Überwachung von Projekten und zur Bewertung ihres Erfolgs anhand von Kennzahlen.","owner": "Kairos Denvin", "img": "static/images/kurse/Project_Control_Strategies.jpg"},
        {"id": 6,"title": "Agiles Arbeiten","short_description": "Lerne agile Methoden wie Scrum und Kanban kennen und verbessere die Zusammenarbeit in Teams.","owner": "Lea Hoffmann","img": "static/images/kurse/AgilesArbeiten.png"},
        {"id": 7,"title": "Datenanalyse mit Python","short_description": "Entdecke, wie du mit Python Daten effizient analysierst und visualisierst.","owner": "Thomas Brandt","img": "static/images/kurse/DatenanalysePython.png"},
        {"id": 8,"title": "Cloud Computing Grundlagen","short_description": "Verstehe die Basis von Cloud-Technologien und wie du sie in deinem Unternehmen einsetzt.","owner": "Clara Vogel","img": "static/images/kurse/CloudComputing.png"},
        {"id": 9,"title": "Digitale Transformation","short_description": "Erfahre, wie digitale Technologien Geschäftsprozesse verändern und neue Chancen schaffen.","owner": "David König","img": "static/images/kurse/DigitaleTransformation.png"},
        {"id": 10,"title": "IT-Projektmanagement","short_description": "Lerne, wie du IT-Projekte effizient planst, steuerst und zum Erfolg führst.","owner": "Sophie Neumann","img": "static/images/kurse/ITProjektmanagement.png"}
        ]
    started=courses = [
        {"id": 1, "title": "Einführung in Machine Learning","short_description":"Ein praxisnaher Einstieg in die Grundlagen des maschinellen Lernens inklusive Klassifikation, Regression und Clustering.","owner": "Felix Schneider", "img": "static/images/kurse/machine_learning.jpg", "progress": 45},
        {"id": 2, "title": "Projektmanagement","short_description":"Erfahre die Grundlagen des Projektmanagements von Planung und Organisation bis hin zu Risikomanagement und erfolgreicher Teamführung.", "owner": "Anna Becker","img": "static/images/kurse/project_management_skill.jpg", "progress": 30},
        {"id": 5, "title":  "Projektcontrolling und Erfolgsmessung","short_description":"Erlerne Techniken zur Überwachung von Projekten und zur Bewertung ihres Erfolgs anhand von Kennzahlen.","owner": "Kairos Denvin", "img": "static/images/kurse/Project_Control_Strategies.jpg", "progress": 20},
        {"id": 6,"title": "Agiles Arbeiten",  "short_description": "Lerne agile Methoden wie Scrum und Kanban kennen und verbessere die Zusammenarbeit in Teams.","owner": "Lea Hoffmann","img": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=600&q=80", "progress": 60}]


    youtube_courses = [
        {
            "id": 1001,
            "title": "Python Tutorial für Anfänger",
            "short_description": "Lerne Python programmieren mit diesem Videokurs für Einsteiger.",
            "owner": "Programming with Mosh",
            "img": "static/images/kurse/python_anfang.jpg",
            "videoId": "_uQrJ0TkZlc",
            "progress": 0
        },
        {
            "id": 1002,
            "title": "Machine Learning Crash Course",
            "short_description": "Google's kompakter Einstieg in maschinelles Lernen.",
            "owner": "Google Developers",
            "img": "static/images/kurse/machine_learning_crash.jpg",
            "videoId": "GwIo3gDZCVQ",
            "progress": 0
        },
        {
            "id": 1003,
            "title": "JavaScript Grundlagen in 60 Minuten",
            "short_description": "Schneller Überblick über JavaScript für Webentwicklung.",
            "owner": "Traversy Media",
            "img": "static/images/kurse/javascript_grundlage.jpg",
            "videoId": "W6NZfCO5SIk",
            "progress": 0
        },
        {
            "id": 1004,
            "title": "HTML & CSS Komplettkurs",
            "short_description": "Lerne Webdesign von Grund auf.",
            "owner": "The Net Ninja",
            "img": "static/images/kurse/html_css_komplett.jpg",
            "videoId": "mU6anWqZJcc",
            "progress": 0
        },
        {
            "id": 1005,
            "title": "React JS Tutorial",
            "short_description": "Erlerne moderne Frontend-Entwicklung mit React.",
            "owner": "Academind",
            "img": "static/images/kurse/reactJs_tutorial.jpg",
            "videoId": "bMknfKXIFA8",
            "progress": 0
        },
        {
            "id": 1006,
            "title": "SQL Grundlagen",
            "short_description": "Verstehe relationale Datenbanken und SQL-Abfragen.",
            "owner": "freeCodeCamp.org",
            "img": "static/images/kurse/sql_grundlage.jpg",
            "videoId": "HXV3zeQKqGY",
            "progress": 0
        }
    ]


    suggested=courses = [{"id": 4, "title": "Supply Chain Management","short_description":"Verstehe die Abläufe in Lieferketten und lerne, wie du Effizienz und Nachhaltigkeit steigerst.","owner": "Mira Solvane", "img": "static/images/kurse/SupplyChainManagement.png"},
                         {"id": 7,"title": "Datenanalyse mit Python","short_description": "Entdecke, wie du mit Python Daten effizient analysierst und visualisierst.","owner": "Thomas Brandt", "img": "static/images/kurse/DatenanalysePython.png"},
                         {"id": 10,"title": "IT-Projektmanagement","short_description": "Lerne, wie du IT-Projekte effizient planst, steuerst und zum Erfolg führst.","owner": "Sophie Neumann","img": "static/images/kurse/ITProjektmanagement.png"},
                         {"id": 8,"title": "Cloud Computing Grundlagen","short_description": "Verstehe die Basis von Cloud-Technologien und wie du sie in deinem Unternehmen einsetzt.","owner": "Clara Vogel","img": "static/images/kurse/CloudComputing.png"},
                         {"id": 9,"title": "Digitale Transformation","short_description": "Erfahre, wie digitale Technologien Geschäftsprozesse verändern und neue Chancen schaffen.","owner": "David König","img": "static/images/kurse/DigitaleTransformation.png"}
                         ]
    name="Thomas"
    l=65
    return render_template("home.html",learn_progress=l,name=name, ongoing=started, empfohlen=suggested, community=courses, youtube_courses=youtube_courses)


@app.route("/suche")
def suche():
    return render_template("course_search.html", courses=courses, learn_progress=65)

@app.route("/favoriten")
def favoriten():
    return render_template("favorites.html")

@app.route("/profil")
def profil():
    return render_template("profile.html")

@app.route("/kurs/<int:course_id>")
def course_detail(course_id):
    all_courses = started + empfohlen + community + youtube_courses  # oder global courses, falls einheitlich
    course = next((c for c in all_courses if c["id"] == course_id), None)
    if course:
        return render_template("course_detail.html", course=course)
    return "Kurs nicht gefunden", 404

if __name__ == "__main__":
    app.run(debug=True)

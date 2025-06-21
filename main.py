from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        {"id": 1, "title": "Einführung in Machine Learning","short_description":"Ein praxisnaher Einstieg in die Grundlagen des maschinellen Lernens inklusive Klassifikation, Regression und Clustering.","owner": "Felix Schneider", "img": "static/images/kurse/Machine_Learning.png"},
        {"id": 2, "title": "Projektmanagement","short_description":"Erfahre die Grundlagen des Projektmanagements von Planung und Organisation bis hin zu Risikomanagement und erfolgreicher Teamführung.", "owner": "Anna Becker","img": "static/images/kurse/Projektmanagement.png"},
        {"id": 3, "title": "Cybersecurity 1","short_description":"Lerne die wichtigsten Methoden zum Schutz von IT-Systemen und Netzwerken gegen Cyberangriffe","owner": "Jonas Weber", "img": "static/images/kurse/CyberSecurity.png"},
        {"id": 4, "title": "Supply Chain Management","short_description":"Verstehe die Abläufe in Lieferketten und lerne, wie du Effizienz und Nachhaltigkeit steigerst.","owner": "Mira Solvane", "img": "static/images/kurse/SupplyChainManagement.png"},
        {"id": 5, "title":  "Projektcontrolling und Erfolgsmessung","short_description":"Erlerne Techniken zur Überwachung von Projekten und zur Bewertung ihres Erfolgs anhand von Kennzahlen.","owner": "Kairos Denvin", "img": "static/images/kurse/Projectcontrolling.png"},
        {"id": 6,"title": "Agiles Arbeiten","short_description": "Lerne agile Methoden wie Scrum und Kanban kennen und verbessere die Zusammenarbeit in Teams.","owner": "Lea Hoffmann","img": "static/images/kurse/AgilesArbeiten.png"},
        {"id": 7,"title": "Datenanalyse mit Python","short_description": "Entdecke, wie du mit Python Daten effizient analysierst und visualisierst.","owner": "Thomas Brandt","img": "static/images/kurse/DatenanalysePython.png"},
        {"id": 8,"title": "Cloud Computing Grundlagen","short_description": "Verstehe die Basis von Cloud-Technologien und wie du sie in deinem Unternehmen einsetzt.","owner": "Clara Vogel","img": "static/images/kurse/CloudComputing.png"},
        {"id": 9,"title": "Digitale Transformation","short_description": "Erfahre, wie digitale Technologien Geschäftsprozesse verändern und neue Chancen schaffen.","owner": "David König","img": "static/images/kurse/DigitaleTransformation.png"},
        {"id": 10,"title": "IT-Projektmanagement","short_description": "Lerne, wie du IT-Projekte effizient planst, steuerst und zum Erfolg führst.","owner": "Sophie Neumann","img": "static/images/kurse/ITProjektmanagement.png"}
        ]
    started=courses = [
        {"id": 1, "title": "Einführung in Machine Learning","short_description":"Ein praxisnaher Einstieg in die Grundlagen des maschinellen Lernens inklusive Klassifikation, Regression und Clustering.","owner": "Felix Schneider", "img": "static/images/kurse/Machine_Learning.png", "progress": 45},
        {"id": 2, "title": "Projektmanagement","short_description":"Erfahre die Grundlagen des Projektmanagements von Planung und Organisation bis hin zu Risikomanagement und erfolgreicher Teamführung.", "owner": "Anna Becker","img": "static/images/kurse/Projektmanagement.png", "progress": 30},
        {"id": 5, "title":  "Projektcontrolling und Erfolgsmessung","short_description":"Erlerne Techniken zur Überwachung von Projekten und zur Bewertung ihres Erfolgs anhand von Kennzahlen.","owner": "Kairos Denvin", "img": "static/images/kurse/Projectcontrolling.png", "progress": 20},
        {"id": 6,"title": "Agiles Arbeiten",  "short_description": "Lerne agile Methoden wie Scrum und Kanban kennen und verbessere die Zusammenarbeit in Teams.","owner": "Lea Hoffmann","img": "static/images/kurse/AgilesArbeiten.png", "progress": 60}]


    youtube_courses = [
        {
            "title": "Python Tutorial für Anfänger",
            "author": "Programming with Mosh",
            "img": "https://i.ytimg.com/vi/_uQrJ0TkZlc/mqdefault.jpg",
            "videoId": "_uQrJ0TkZlc"
        },
        {
            "title": "Machine Learning Crash Course",
            "author": "Google Developers",
            "img": "https://i.ytimg.com/vi/GwIo3gDZCVQ/mqdefault.jpg",
            "videoId": "GwIo3gDZCVQ"
        },
        {
            "title": "JavaScript Grundlagen in 60 Minuten",
            "author": "Traversy Media",
            "img": "https://i.ytimg.com/vi/W6NZfCO5SIk/mqdefault.jpg",
            "videoId": "W6NZfCO5SIk"
        },
        {
            "title": "HTML & CSS Komplettkurs",
            "author": "The Net Ninja",
            "img": "https://i.ytimg.com/vi/mU6anWqZJcc/mqdefault.jpg",
            "videoId": "mU6anWqZJcc"
        },
        {
            "title": "React JS Tutorial",
            "author": "Academind",
            "img": "https://i.ytimg.com/vi/bMknfKXIFA8/mqdefault.jpg",
            "videoId": "bMknfKXIFA8"
        },
        {
            "title": "SQL Grundlagen",
            "author": "freeCodeCamp.org",
            "img": "https://i.ytimg.com/vi/HXV3zeQKqGY/mqdefault.jpg",
            "videoId": "HXV3zeQKqGY"
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
    return render_template("search.html")

@app.route("/favoriten")
def favoriten():
    return render_template("favorites.html")

@app.route("/profil")
def profil():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)

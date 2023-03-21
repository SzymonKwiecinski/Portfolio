from flask import Flask, render_template, abort
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.portfolioDB
    projects = [project for project in app.db.projectsColl.find({})]
    slug_to_project = {project['slug']: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)

    @app.route("/about")
    def about():
        return render_template('about.html')

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/description")
    def description():
        return render_template("description.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template("project.html", project=slug_to_project[slug])

    return app

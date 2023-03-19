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
    print(projects)
    slug_to_project = {project['slug']: project for project in projects}
    print(slug_to_project)


#
# projects = [
#     {
#         "name": "Habit tracking app with Python and MongoDB",
#         "text": "lapis habit",
#         "thumb": "img/habit-tracking.png",
#         "hero": "img/habit-tracking-hero.png",
#         "categories": ["python", "web"],
#         "slug": "habit-tracking",
#         "prod": "https://udemy.com",
#     },
#     {
#         "name": "Personal finance tracking app with React",
#         "text": "lapis personal",
#         "thumb": "img/personal-finance.png",
#         "hero": "img/personal-finance.png",
#         "categories": ["react", "javascript"],
#         "slug": "personal-finance",
#     },
#     {
#         "name": "REST API Documentation with Postman and Swagger",
#         "text": "lapis rest api",
#         "thumb": "img/rest-api-docs.png",
#         "hero": "img/rest-api-docs.png",
#         "categories": ["writing"],
#         "slug": "api-docs",
#     },
# ]
#
# slug_to_projectect = {project['slug']: project for project in projects}

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
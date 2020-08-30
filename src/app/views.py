from flask import Flask, jsonify, request
from .db.models import Person
from mongoengine.errors import ValidationError
from json import loads
import os


def init(app: Flask):
    @app.route("/")
    def index():
        app_name = os.getenv("APP_NAME")
        if app_name:
            return f"Hello from {app_name} running in Docker!"
        return "Hello from flask!"

    @app.route("/people", methods=["GET", "POST"])
    def people():
        if request.method == "POST":
            if not request.is_json:
                return jsonify({"message": "please post valid JSOn!"}), 400

            body = request.json
            p = Person(**body)
            try:
                p.save()
            except ValidationError as e:
                return jsonify(e.to_dict()), 400
            return p.to_json(), 201

        else:
            data = [loads(f.to_json()) for f in Person.objects]
            return jsonify(data), 200

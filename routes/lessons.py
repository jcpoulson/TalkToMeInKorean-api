from flask import json
from flask.json import jsonify
from . import api
from mongo_handler.get_lesson import get_lesson
from mongo_handler.get_levels import get_levels


@api.route('/levels', methods=["GET"])
def all_levels():
    all_content = get_levels()
    return jsonify(all_content)


@api.route('/lessons/<int:level>/<string:lesson>', methods=["GET"])
def get_level_lesson(level, lesson):
    mongo_level_lesson = get_lesson(level, lesson)
    return jsonify(mongo_level_lesson)
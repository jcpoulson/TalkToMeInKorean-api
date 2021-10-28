from . import api
from mongo_handler.get_lesson import get_lesson
from mongo_handler.get_levels import get_levels


@api.route('/levels', methods=["GET"])
def all_levels():
    all_content = get_levels()
    return all_content


@api.route('/lessons/<int:level>/<int:lesson>', methods=["GET"])
def get_level_lesson(level, lesson):
    # Just keep in mind when accessing url params, it is done through the 
    # route parameters
    mongo_level_lesson = get_lesson(level, lesson)
    return mongo_level_lesson
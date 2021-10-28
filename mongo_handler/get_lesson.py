from . import client

def get_lesson(level, lesson):
    db = client.ttmik
    levels = db.levels
    selected_level = levels.find_one({"level": level})

    try:
        return selected_level['lessons'][f'lesson{lesson}']
    except Exception:
        return "Unable to connect to the server."






# Huge thing to remember that gave me a bunch of issues here
# When accessing an dictionary(very JS object like)'s properties
# you don't access it like in JS with <Object.property>
# In Python you would access an objects properties like this

# <Dictionary['property']['additional_property']>
# user['email']

# A dictionary is a data structure not an object, they are not the same thing


from . import client

def get_levels():
    db = client.ttmik
    levels = db.levels.find({}).sort("level", 1) # MongoDB sorts things pretty weird by default, this puts the levels in ascending orders

    levels_list = list(levels)
    levels_dict = {}

    for index, level in enumerate(levels_list):
        level.pop('_id')
        levels_dict[index + 1] = level

    return levels_dict
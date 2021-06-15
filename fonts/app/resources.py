import json
import os

DIR_RESOURCES = 'resources'

PATH_EMOTION_FONTS = os.path.join(DIR_RESOURCES, 'emotion_fonts.json')


def load_emotion_fonts() -> dict[str, list[str]]:
    with open(PATH_EMOTION_FONTS) as file_emotion_fonts:
        return json.load(file_emotion_fonts)

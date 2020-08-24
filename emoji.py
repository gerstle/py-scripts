import yaml
import random
import pathlib
import sys


def get_emoji(emoji_type):
    with open(pathlib.Path(__file__).parent / 'emojis.yml') as file:
        try:
            emojis = yaml.load(file, Loader=yaml.FullLoader)
            print(random.choice(emojis[emoji_type]))
        except Exception as e:
            print("couldn't find emoji type " + emoji_type)


get_emoji('animals' if len(sys.argv) == 1 else sys.argv[1])

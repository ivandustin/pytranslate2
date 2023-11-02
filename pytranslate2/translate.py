from functools import partial
from pathlib import Path
from pyopenaichat import system, user, chat
from .definition.get import get as get_definition
from .constants.commands import TRANSLATE
from .split import split


def translate(dictionary: Path, text: str):
    words = split(text)
    definitions = map(partial(get_definition, dictionary), words)
    context = list(map(system, definitions))
    messages = context + [user(text.lower())] + [user(TRANSLATE)]
    response = chat(messages)
    return response["content"]

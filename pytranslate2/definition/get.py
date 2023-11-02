from pathlib import Path
from pydefine.get_group import get_group
from pytranslate2.constants.extensions import TXT
from pytranslate2.file.read import read


def get(dictionary: Path, word: str):
    group = get_group(word)
    filename = word + TXT
    filepath = dictionary / group / filename
    return read(filepath)

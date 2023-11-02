from pathlib import Path
from pytranslate2.constants.encodings import UTF8


def read(filepath: Path):
    return filepath.read_text(encoding=UTF8)

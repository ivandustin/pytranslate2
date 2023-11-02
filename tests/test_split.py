from pytranslate2.split import split


def test():
    assert split("hello world") == ["hello", "world"]

from os import remove
from terre.util.array import concat
from terre.util.day import now_stamp
from terre.util.fs import save_json
from terre.util.fs import save_file
from terre.util.fs import read_file


def test_concat():
    a = [
        "hello",
        "world",
        "do",
        "you",
        "like",
        "this?"
    ]

    b = [
        "yes",
        "I",
        "like",
        "this",
        "machine",
        8,
        8,
        6
    ]

    c = concat(a, b)
    assert (len(a) + len(b)) == len(c)


def test_now():
    assert len(str(now_stamp())) == 13


def test_save_json():
    filename = "test-file"
    json_str = {"hello": "world"}
    filepath = save_json(filename, json_str)

    assert filepath == filename + '.json'
    assert read_file(filepath) == '{\n"hello": "world"\n}'

    remove(filepath)


def test_save_file():
    filepath = "test-file"
    raw_text = "hello, world"

    assert save_file(filepath, raw_text) == filepath
    assert read_file(filepath) == raw_text

    remove(filepath)

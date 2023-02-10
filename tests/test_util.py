from terre.util.array import concat
from terre.util.day import now_stamp


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
    assert len(now_stamp()) == 13

from usine.util.array import concat


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

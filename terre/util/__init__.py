from json import dumps
from json import load


def save_json(filename: str, data: any, **kw):
    """
    :Args:
      - filename: filename to be saved
      - data: data to be output
    """
    indent = kw.get("indent") or 0
    with open(filename, "w", encoding="utf-8") as f:
        f.write(dumps(data, ensure_ascii=False, indent=indent))


def read_json(filename: str, **kw):
    with open(filename, "r", encoding="utf-8") as f:
        return load(f)


def read_file(filename: str, **kw):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

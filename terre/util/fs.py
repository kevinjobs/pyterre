from json import dumps
from json import load


def save_json(filename: str, data: any, **kw):
    """
    :Args:
      - filename: filename to be saved
      - data: data to be output
    """
    indent = kw.get("indent") or 0
    json_str = dumps(data, ensure_ascii=False, indent=indent)
    filepath = f"{filename}.json"
    return save_file(filepath, json_str, **kw)


"""
def save_picture(filename: str, data: any, ext: str, **kw):
    save_file(f"{filename}.{ext}", data, encoding=None, **kw)
"""


def save_file(filepath: str, data: any, **kw):
    mode = kw.get("mode") or "w"
    encoding = kw.get("encoding") or "utf-8"
    with open(filepath, mode=mode, encoding=encoding) as f:
        f.write(data)
    return filepath


def read_file(filename: str, **kw):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

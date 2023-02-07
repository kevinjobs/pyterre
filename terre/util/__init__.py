from json import dumps


def save_json(filename: str, data: any, **kw) -> None:
    """
    :Args:
      - filename: filename to be saved
      - data: data to be output
    """
    indent = kw.get("indent") or 0
    with open(filename, "w", encoding="utf-8") as f:
        f.write(dumps(data, ensure_ascii=False, indent=indent))

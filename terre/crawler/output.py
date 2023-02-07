from json import dumps
from json import load
import typing as t


class Output:
    @staticmethod
    def save_json(filename: str, data: t.Any, **kw) -> None:
        """
        :Args:
          - filename: filename to be saved
          - data: data to be output
        """
        indent = kw.get("indent") or 0
        with open(filename, "w", encoding="utf-8") as f:
            f.write(dumps(data, ensure_ascii=False, indent=indent))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def read_json(filename: str) -> t.Union[dict, list]:
        with open(filename, "r", encoding="utf-8") as f:
            return load(f)

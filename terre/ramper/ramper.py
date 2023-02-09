from typing import Generator
from terre.util import save_json as save
from .item import RamperItem


class Ramper:
    def __init__(self):
        self.data: Generator[RamperItem] = self.parse()

    def parse(self):
        raise NotImplementedError

    def filter(self):
        pass

    def to_json(self):
        _data = [data.to_dict() for data in self.data]
        if len(_data) == 1:
            return _data[0]
        return _data

    def save_json(self, filename: str):
        save(filename, self.to_json())

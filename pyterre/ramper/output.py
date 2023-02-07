from pyterre.util import save_json
from datetime import datetime


class Output:
    def __init__(self, data: any, **kw):
        self.data = data
        self.filename = kw.get("filename") \
            or f"ramper_output_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    def save(self):
        save_json(self.filename, self.data)

    def to_dict(self):
        pass

    def to_json(self):
        pass

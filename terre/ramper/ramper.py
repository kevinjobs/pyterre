from typing import Optional
from terre.ramper.output import Output


class Ramper:
    def __init__(self):
        self.data = None
        self.op: Optional[Output] = None

    def run(self):
        self.before_start()
        self.data = self.start()
        self.after_start()

        self.before_filter()
        self.filter()
        self.after_filter()

        self.before_output()
        self.output()
        self.after_output()

    def start(self):
        raise NotImplementedError

    def filter(self):
        pass

    def output(self, **kw):
        op = Output(self.data, **kw)
        op.save()

    def before_start(self):
        pass

    def after_start(self):
        pass

    def before_filter(self):
        pass

    def after_filter(self):
        pass

    def before_output(self):
        pass

    def after_output(self):
        pass

    def to_dict(self):
        return self.op.to_dict()

    def to_json(self):
        return self.op.to_json()

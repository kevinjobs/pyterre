from usine_ramper.output import Output


class Ramper:
    def __init__(self):
        self.op: Output = None

    def run(self):
        pass

    def start(self):
        pass

    def filter(self):
        pass

    def output(self, **kw):
        op = Output(**kw)
        self.before_output()
        op.save()
        self.after_output()

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

    def to_data(self):
        pass

    def to_json(self):
        pass

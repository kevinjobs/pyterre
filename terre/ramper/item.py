class RamperItem:
    """ramper item"""
    def to_dict(self):
        d = {}
        for k, v in vars(self).items():
            d[k] = v
        return d

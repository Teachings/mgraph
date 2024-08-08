class State:
    def __init__(self):
        self.data = {}

    def update(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def __repr__(self):
        return str(self.data)

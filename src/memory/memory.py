class Memory:
    def __init__(self):
        self.items = []

    def add(self, content):
        self.items.append(content)

    def recent(self, limit=10):
        return self.items[-limit:]

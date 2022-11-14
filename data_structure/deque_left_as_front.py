class Deque(object):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        self.items.pop(0)

    def remove_rear(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
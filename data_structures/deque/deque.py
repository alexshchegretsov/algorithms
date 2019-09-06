
class Deque:
    def __init__(self):
        self.items = []

    def push_end(self, v):
        self.items.append(v)

    def push_first(self, v):
        self.items.insert(0, v)

    def pop_first(self):
        if self.items:
            return self.items.pop(0)

    def pop_end(self):
        if self.items:
            return self.items.pop()

    def print_deque(self):
        print(self.items)


d = Deque()
d.push_first(2)
d.push_first(3)
d.push_end(4)
d.push_end(7)
d.pop_first()
d.pop_end()
d.print_deque()

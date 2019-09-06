class Stack:
    def __init__(self):
        self.items = []

    def push_item(self, v):
        self.items.append(v)

    def pop_item(self):
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def show_end(self):
        if self.items:
            print(self.items[-1])


s = Stack()
s.push_item(5)
s.push_item(7)
s.push_item(-1)
s.pop_item()
s.print_stack()
s.show_end()

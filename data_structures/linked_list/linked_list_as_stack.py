class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


class Stack:
    def __init__(self, capacity=10):
        self.last = Node()
        self.capacity = capacity

    def get_length(self):
        curr = self.last.nxt
        i = 0
        while curr:
            i += 1
            curr = curr.nxt
        return i

    def push(self, v):
        if self.get_length() < self.capacity:
            new_node = Node(v)
            nxt = self.last.nxt
            self.last.nxt = new_node
            new_node.nxt = nxt

    def pop(self):
        if self.last.nxt:
            p = self.last.nxt
            self.last.nxt = self.last.nxt.nxt
            return p

    def __str__(self):
        curr = self.last.nxt
        while curr:
            print(curr.v, end=' <- ')
            curr = curr.nxt
        return ''


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(3)
    # s.pop()

    print(s)
    print(s.get_length())
    for i in range(10):
        s.push(i)
    print(s)
    print(s.get_length())

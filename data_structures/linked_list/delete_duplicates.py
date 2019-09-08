class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def print_nodes(node: Node):
    while node:
        print(node.v, end=' -> ')
        node = node.nxt


def del_duplicate(node: Node):
    while node.nxt:
        if node.v == node.nxt.v:
            node.nxt = node.nxt.nxt
            continue
        node = node.nxt


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(1)
    n3 = Node(1)
    n4 = Node(2)
    n5 = Node(3)
    n6 = Node(4)

    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4
    n4.nxt = n5
    n5.nxt = n6

    print_nodes(n1)
    del_duplicate(n1)
    print()
    print_nodes(n1)

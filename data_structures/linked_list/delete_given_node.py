class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def delete(node: Node):
    while node.nxt:
        if not node.nxt.nxt:
            nxt = node.nxt
            node.nxt = None
            node.v = nxt.v
            break
        node.v = node.nxt.v
        node = node.nxt



def print_nodes(node: Node):
    while node:
        print(node.v, end=' -> ')
        node = node.nxt


if __name__ == '__main__':
    n1 = Node(4)
    n2 = Node(5)
    n3 = Node(1)
    n4 = Node(9)
    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4

    print_nodes(n1)
    delete(n2)
    print()
    print_nodes(n1)

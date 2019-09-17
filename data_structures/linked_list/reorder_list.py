class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None

def print_nodes(node: Node):
    while node:
        print(node.v, end= ' - ')
        node = node.nxt
    print()

def reorder(head: Node):
    prev = None
    node = head

    while node.nxt:
        nxt = node.nxt
        p = nxt
        if not p.nxt:
            break
        while p.nxt:
            prev = p
            p = p.nxt

        prev.nxt = None
        node.nxt = p
        p.nxt = nxt
        node = nxt




if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    # n6 = Node(6)

    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4
    n4.nxt = n5
    # n5.nxt = n6
    print_nodes(n1)
    reorder(n1)
    print_nodes(n1)

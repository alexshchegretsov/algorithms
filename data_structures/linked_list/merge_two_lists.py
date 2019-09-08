class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def print_nodes(node: Node):
    while node:
        print(node.v, end=' -> ')
        node = node.nxt
    print()


def merge_2(node_1: Node, node_2: Node):
    dummy = Node()
    head = dummy
    while node_1 and node_2:
        if node_1.v < node_2.v:
            dummy.nxt = node_1
            node_1 = node_1.nxt
        else:
            dummy.nxt = node_2
            node_2 = node_2.nxt
        dummy = dummy.nxt
    if node_1:
        dummy.nxt = node_1
    if node_2:
        dummy.nxt = node_2
    return head.nxt


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)

    n4 = Node(2)
    n5 = Node(3)
    n6 = Node(4)
    n7 = Node(8)

    n1.nxt = n2
    n2.nxt = n3

    n4.nxt = n5
    n5.nxt = n6
    n6.nxt = n7

    print_nodes(n1)
    print_nodes(n4)
    p = merge_2(n1,n4)
    print_nodes(p)
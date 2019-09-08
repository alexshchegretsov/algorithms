class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def reverse_list(node: Node):
    if not node.nxt:
        return node
    reverse_list(node.nxt)
    node.nxt.nxt = node
    node.nxt = None


def print_node(node: Node):
    while node:
        print(node.v, end=' -> ')
        node = node.nxt


def get_length(node: Node):
    return 0 if not node else get_length(node.nxt) + 1


def insert(index: int, node: Node, val: int):
    new_node = Node(val)
    length = get_length(node)
    if index >= length:
        raise IndexError
    elif 0 <= index < length:
        # tmp = None
        while index-1:

            node = node.nxt
            tmp = node.nxt
            index -= 1
        node.nxt = new_node
        new_node.nxt = tmp


if __name__ == '__main__':
    head = Node()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    # head.nxt = n1
    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4

    print_node(n1)
    # reverse_list(n1)
    # print_node(n4)
    print()
    insert(2, n1, 7)
    print_node(n1)

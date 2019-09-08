class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def just_print(node: Node):
    while node:
        print(node.v, end=' -> ')
        node = node.nxt


def rec_print(node: Node):
    if not node:
        return
    rec_print(node.nxt)
    print(node.v, end=' -> ')
    # if node:
    #     rec_print(node.nxt)
    #     print(node.v, end=' -> ')
    # return node
    #


def reverse(node: Node) -> Node:
    print(f'node value: {node.v}')
    if not node.nxt:
        print(f'return node: {node.v}')
        return node
    else:
        p = reverse(node.nxt)
        print(f'p is {p.v}')
        print(f'node.nxt.nxt: {node.nxt.nxt}, node.v: {node.v}')
        node.nxt.nxt = node
        print(f'node.nxt.nxt after = node : {node.nxt.nxt.v}')
        print(f'node.nxt: {node.nxt.v}')
        node.nxt = None
    return p

if __name__ == '__main__':
    head = Node()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    head.nxt = n1
    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4


    p = reverse(n1)
    # just_print(n4)
    print(p.nxt.v)

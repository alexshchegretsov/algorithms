class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def is_pal(node: Node):
    # method 1
    # tmp = []
    # while node:
    #     tmp.append(node.v)
    #     node = node.nxt
    # print(tmp)
    # print(tmp == tmp[::-1])

    # method 2
    p = node
    stack = []
    while node:
        stack.append(node.v)
        node = node.nxt
    while p:
        if p.v != stack.pop():
            return False
        p = p.nxt
    return True



def get_length(node: Node):
    if not node:
        return 0
    return get_length(node.nxt) + 1


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(1)
    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4
    print(is_pal(n1))
    print(get_length(n1))

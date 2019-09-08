class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def print_nodes(head: Node):
    curr = head
    while curr.nxt:
        print(f'{curr.v}', end=' -> ')
        curr = curr.nxt
    print(f'{curr.v} -> {curr.nxt}')


def reverse_nodes(head: Node):
    if not head:
        return
    prev = None
    curr = head
    while curr:
        nxt = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = nxt
    return prev



if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4
    n4.nxt = n5
    print_nodes(n1)
    rev_head = reverse_nodes(n1)
    print_nodes(rev_head)

class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


def print_nodes(node: Node):
    curr = node
    while curr:
        print(curr.v, end=' - ')
        curr = curr.nxt

def find_length(node: Node):
    curr = node
    i = 0
    while curr:
        i += 1
        curr = curr.nxt
    return i

def start_point(node: Node, diff: int):
    curr = node
    while diff:
        curr = curr.nxt
        diff -= 1
    return curr

def solution(head_a: Node, head_b: Node):
    if not head_a or not head_b:
        return
    len_a = find_length(head_a)
    len_b = find_length(head_b)
    diff = abs(len_a - len_b)
    if len_a > len_b:
        head_a = start_point(head_a, diff)
    elif len_b > len_a:
        head_b = start_point(head_b, diff)
    if head_a is head_b:
        return head_a
    p = find_intersection(head_a, head_b)
    return p

def find_intersection(head_1: Node, head_2: Node):
    while head_1 and head_2:
        if head_1.nxt is head_2.nxt:
            return head_1.nxt
        head_1 = head_1.nxt
        head_2 = head_2.nxt
    return

if __name__ == '__main__':
    n1_c = Node(-1)
    n2_c = Node(-2)
    n1_c.nxt = n2_c

    n1_a = Node(10)
    n2_a = Node(21)
    n3_a = Node(15)
    n4_a = Node(34)
    n1_a.nxt = n2_a
    n2_a.nxt = n3_a
    n3_a.nxt = n4_a
    n4_a.nxt = n1_c

    n1_b = Node(2)
    n2_b = Node(4)
    n3_b = Node(9)
    n1_b.nxt = n2_b
    n2_b.nxt = n3_b
    n3_b.nxt = n1_c

    print_nodes(n1_a)
    print()
    print_nodes(n1_b)
    print()
    p = solution(n1_a, n1_b)
    print(p, p.v)
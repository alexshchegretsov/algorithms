from collections import deque


class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def print_nodes(node: Node):
    if node:
        print(node.v)

        print_nodes(node.left)
        print_nodes(node.right)


def iterative_invertion(node: Node):
    dq = deque()
    dq.append(node)
    while dq:
        curr = dq.popleft()
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            dq.append(curr.left)
        if curr.right:
            dq.append(curr.right)
    return node


def __recursive_invertion(node: Node):
    if not node:
        return
    __recursive_invertion(node.left)
    __recursive_invertion(node.right)
    node.left, node.right = node.right, node.left
    return node


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print_nodes(root)
    print()
    p = iterative_invertion(root)
    print_nodes(p)

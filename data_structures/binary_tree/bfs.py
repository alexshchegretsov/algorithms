class Node:
    def __init__(self, v=None):
        self.v = v
        self.left = None
        self.right = None


def search(node: Node, target: int):
    if not node:
        return
    if node.v == target:
        return node
    if node.v < target:
        return search(node.right, target)
    else:
        return search(node.left, target)


def insert(root: Node, node: Node):
    if root.v < node.v:
        if not root.right:
            root.right = node
        else:
            insert(root.right, node)
    elif root.v > node.v:
        if not root.left:
            root.left = node
        else:
            insert(root.left, node)


def breadth_first_search(node: Node):
    nodes = []
    queue = [node]
    while queue:
        curr = queue.pop(0)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        nodes.append(curr.v)
    return nodes


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(14)
    root.left.left = Node(5)
    root.right.right = Node(20)

    print(breadth_first_search(root))

    insert(root, Node(12))
    insert(root, Node(-3))
    insert(root, Node(34))
    print(breadth_first_search(root))

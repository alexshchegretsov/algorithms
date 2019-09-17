class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

def print_nodes(node: Node):
    if node:

        print_nodes(node.left)
        print(node.v)

        print_nodes(node.right)

def find_sum(node: Node, summ=0):
    if not node:
        return summ
    x = find_sum(node.left, node.v+summ)

    y = find_sum(node.right, node.v+summ)
    

    if 20 == y:
        return True


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    # print_nodes(root)
    print(find_sum(root))
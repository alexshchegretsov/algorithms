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


class Solution:
    def __init__(self):
        self.subtree = None
        self.subtree_sum = float('inf')

    def min_sum(self, node: Node):
        self.__min_sum(node)
        return self.subtree

    def __min_sum(self, node: Node):
        if not node:
            return 0
        summ = self.__min_sum(node.left) + self.__min_sum(node.right) + node.v
        if summ < self.subtree_sum:
            self.subtree_sum = summ
            self.subtree = node
        return summ


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    s = Solution()
    p = s.min_sum(root)
    print_nodes(p)
    print(s.subtree_sum)
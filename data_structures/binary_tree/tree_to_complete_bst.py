class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


class ConvertToCompleteBST:
    def convert(self, a: list) -> Node:
        start, end = 0, len(a) - 1
        return self.__convert(start, end, a)

    def __convert(self, start: int, end: int, a: list):
        if start > end:
            return
        mid = (start + end) // 2
        root = Node(a[mid])
        root.left = self.__convert(start, mid - 1, a)
        root.right = self.__convert(mid + 1, end, a)
        return root

    def display_tree(self, node: Node):
        if node:
            print(node.v)
            self.display_tree(node.left)

            self.display_tree(node.right)




if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    s = ConvertToCompleteBST()
    root = s.convert(a)
    s.display_tree(root)

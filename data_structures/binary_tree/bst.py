class Node:
    def __init__(self, v=None):
        self.v = v
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):
        if not self.root:
            self.root = Node(v)
        else:
            self._insert(v, self.root)

    def _insert(self, v, node: Node):
        if v < node.v:
            if not node.left:
                node.left = Node(v)
                node.left.parent = node  # set parent
            else:
                self._insert(v, node.left)
        else:
            if not node.right:
                node.right = Node(v)
                node.right.parent = node # set parent
            else:
                self._insert(v, node.right)

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, node: Node):
        if node:
            self._print_tree(node.left)
            print(node.v)
            self._print_tree(node.right)

    def height(self) -> int:
        return self._height(self.root, 0) if self.root else 0

    def _height(self, node: Node, curr_height: int):
        if not node:
            return curr_height
        left = self._height(node.left, curr_height + 1)
        right = self._height(node.right, curr_height + 1)
        return max(left, right)

    def minimum(self):
        return self._minimum(self.root.left) if self.root.left else self.root.v

    def _minimum(self, node: Node):
        if not node.left:
            return node.v
        left = self._minimum(node.left)
        return left

    def maximum(self):
        return self._maximum(self.root.right) if self.root.right else self.root

    def _maximum(self, node: Node):
        if not node.right:
            return node.v
        right = self._maximum(node.right)
        return right

    def search(self, v):
        return self._search(self.root, v) if self.root else False

    def _search(self, node: Node, v: int):
        if node.v == v:
            return True
        elif v < node.v and node.left:
            return self._search(node.left, v)
        elif v > node.v and node.right:
            return self._search(node.right, v)
        return False

    def find(self, v):
        return self._find(self.root, v) if self.root else None


    def _find(self, node: Node, v):
        if v == node.v:
            return node
        elif v < node.v and node.left:
            return self._find(node.left, v)
        elif v > node.v and node.right:
            return self._find(node.right, v)
        return False

    def delete_value(self, v):
        self.delete_node(self.find(v))

    def delete_node(self, node: Node):

        # returns min node in tree rooted as input node
        def min_value_node(node: Node):
            curr = node
            while curr:
                curr = curr.left
            return curr

        # returns th number of children of the specified node
        def amount_child(node: Node):
            amount = 0
            if node.left:
                amount += 1
            if node.right:
                amount += 1
            return amount

        # get the parent of the node to be deleted
        parent_node = node.parent

        # get the number of children of the node to be deleted
        num_child = amount_child(node)

        # break operation into different cases based on
        # tree structre & node to be deleted

        if not num_child:
            # remove reference to the node from the parent
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None
        # CASE 2 (node has a single child)
        if num_child == 1:

            # get the single child node
            child = node.left if node.left else node.right

            # replece the node to be deleted to its child
            if parent_node.left == node:
                parent_node.left = child
            else:
                parent_node.right = child

            # correct the child parent pointer
            child.parent = parent_node

        # CASE 3 (node has two children)
        if num_child == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node)

            # copy the inorder successor's value to the node formerly
            # holding the value we want to be delete
            node.v = successor.v

            # delete the inorder successor now that it's values was
            # copied into another node
            self.delete_node(successor)


if __name__ == '__main__':
    b = BST()
    b.insert(10)
    b.insert(12)
    b.insert(2)
    b.insert(8)
    b.insert(9)
    b.insert(15)
    b.insert(0)
    b.insert(-7)
    b.insert(-2)
    b.insert(7)
    b.insert(94)
    b.insert(95)
    b.insert(14)
    # b.print_tree()
    print(b.height())
    print(b.minimum())
    print(b.maximum())
    print(b.search(0))

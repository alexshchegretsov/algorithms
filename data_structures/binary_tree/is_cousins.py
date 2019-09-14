class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self, v):
        self.root = Node(v)

    def insert_value(self, v):
        self.__insert_value(self.root, v)

    def __insert_value(self, node: Node, v):
        if v < node.v:
            if not node.left:
                node.left = Node(v)
                node.left.parent = node
            else:
                self.__insert_value(node.left, v)
        else:
            if not node.right:
                node.right = Node(v)
                node.right.parent = node
            else:
                self.__insert_value(node.right, v)

    def print_tree(self):
        self.__print_tree(self.root)

    def __print_tree(self, node: Node):
        if not node:
            return
        self.__print_tree(node.left)
        print(node.v)
        self.__print_tree(node.right)

    def own_height(self, v):
        return self.__own_height(self.root, v, 0)

    def __own_height(self, node: Node, v, curr_height):
        if v == node.v:
            return curr_height
        elif v < node.v and node.left:
            return self.__own_height(node.left, v, curr_height + 1)
        elif v > node.v and node.right:
            return self.__own_height(node.right, v, curr_height + 1)

    def find_node(self, v):
        return self.__find_node(self.root, v)

    def __find_node(self, node: Node, v):
        if v == node.v:
            return node
        elif v < node.v and node.left:
            return self.__find_node(node.left, v)
        elif v > node.v and node.right:
            return self.__find_node(node.right, v)


    def is_cousins(self, v_1, v_2):
        node_1 = self.find_node(v_1)
        node_2 = self.find_node(v_2)
        if node_2 and node_1:
            if not node_2.parent is node_1.parent:
                node_1_height = self.own_height(v_1)
                node_2_height = self.own_height(v_2)
                return node_2_height == node_1_height
        return False



if __name__ == '__main__':
    b = BST(10)
    b.insert_value(5)
    b.insert_value(15)
    b.insert_value(0)
    b.insert_value(23)
    b.print_tree()
    p = b.find_node(23)
    # print(type(p))
    # print(b.own_height(15))

    print(b.is_cousins(3, 23))

    """
        10
       /  \
      5    15
     /      \
    0        23
       
       
    """

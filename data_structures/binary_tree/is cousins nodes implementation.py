from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        parent_x = self.find_parent(root, x)
        parent_y = self.find_parent(root, y)
        if not parent_x is parent_y:
            height_x = self.height(root, x, 0)
            height_y = self.height(root, y, 0)
            return height_x == height_y
        return False

    def find_parent(self, node: TreeNode, v, parent=None):
        if v == node.val:
            return parent
        elif v < node.val and node.left:
            # parent = node
            return self.find_parent(node.left, v, node)
        elif v > node.val and node.right:
            # parent = node
            return self.find_parent(node.right, v, node)

    def height(self, node: TreeNode, v, curr_height):
        if v == node.val:
            return curr_height
        elif v < node.val and node.left:
            return self.height(node.left, v, curr_height + 1)
        elif v > node.val and node.right:
            return self.height(node.right, v, curr_height + 1)


class BinarySolution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent_x = self.find_parent(root, x)
        parent_y = self.find_parent(root, y)
        if parent_y and parent_x:
            if not parent_y is parent_x:
                height_x = self.height(root, x, 0)
                height_y = self.height(root, y, 0)
                return height_y == height_x
        return False

    def find_parent(self, node: TreeNode, v):
        dq = deque()
        dq.append(node)
        while dq:
            curr_node = dq.popleft()
            if curr_node.left:
                if curr_node.left.val == v:
                    return curr_node
                dq.append(curr_node.left)
            if curr_node.right:
                if curr_node.right.val == v:
                    return curr_node
                dq.append(curr_node.right)

    def height(self, node: TreeNode, v, curr_height):
        if not node:
            return
        if v == node.val:
            return curr_height
        down_level = self.height(node.left, v, curr_height + 1)
        if down_level:
            return down_level
        down_level = self.height(node.right, v, curr_height + 1)
        return down_level


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    # root.right.right = TreeNode(5)
    s = BinarySolution()
    # p = s.find_parent(root, 7)
    # print(p)
    print(s.height(root, 3, 0))
    print(s.height(root, 4, 0))
    print(s.find_parent(root, 3).val)
    print(s.find_parent(root, 4).val)
    # print(s.isCousins(root, 3, 4))

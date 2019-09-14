from collections import deque

class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        self.parent = None

def bfs(node: Node):
    nodes = []
    dq = deque()
    dq.append(node)
    while dq:
        curr_node = dq.popleft()
        nodes.append(curr_node.v)
        if curr_node.left:
            dq.append(curr_node.left)
        if curr_node.right:
            dq.append(curr_node.right)
    return nodes

def dfs(node: Node):
    pass

def insert_node(root: Node, node: Node):
    if node.v < root.v:
        if not root.left:
            root.left = node
            node.parent = root
        else:
            insert_node(root.left, node)
    else:
        if not root.right:
            root.right = node
            node.parent = root
        else:
            insert_node(root.right, node)


def print_nodes(node: Node):
    if not node:
        return
    print(node.v)
    print_nodes(node.left)
    print_nodes(node.right)


def print_traversals(node: Node, traversal_type: str):
    if traversal_type == 'pre_order':
        return __pre_order(node, '')
    elif traversal_type == 'in_order':
        return __in_order(node, '')
    elif traversal_type == 'post_order':
        return __post_order(node, '')


def __post_order(node: Node, traversal):
    if node:
        traversal = __post_order(node.left, traversal)
        traversal = __post_order(node.right, traversal)
        traversal += f'{node.v} - '
    return traversal


def __in_order(node: Node, traversal):
    if node:
        traversal = __in_order(node.left, traversal)
        traversal += f'{node.v} - '
        traversal = __in_order(node.right, traversal)
    return traversal


def __pre_order(node: Node, traversal: str):
    if node:
        traversal += f'{node.v} - '
        traversal = __pre_order(node.left, traversal)
        traversal = __pre_order(node.right, traversal)
    return traversal


def find_node(node: Node, v: int):
    if not node:
        return
    if node.v == v:
        return node
    elif v < node.v:
        return find_node(node.left, v)
    elif v > node.v:
        return find_node(node.right, v)


def find_successor(node: Node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr


def child_amount(node: Node):
    amount = 0
    if node.left:
        amount += 1
    if node.right:
        amount += 1
    return amount


def delete_node(node: Node):
    if not node:
        return
    amount = child_amount(node)
    parent_node = node.parent

    # 1st case - no children
    if not amount:
        if parent_node.left == node:
            parent_node.left = None
        else:
            parent_node.right = None


    # 2nd case - 1 children
    elif amount == 1:
        child = node.left if node.left else node.right
        if parent_node.left == node:
            parent_node.left = child
        else:
            parent_node.right = child

        child.parent = parent_node
    # 3rd case - 2 children
    elif amount == 2:
        successor = find_successor(node.right)
        node.v = successor.v
        delete_node(successor)


if __name__ == '__main__':
    root = Node(20)
    insert_node(root, Node(35))
    insert_node(root, Node(9))
    insert_node(root, Node(24))
    insert_node(root, Node(0))
    insert_node(root, Node(10))
    # print_nodes(root)
    # p = find_node(root, 9)
    # delete_node(p)
    # print_nodes(root)
    # print(print_traversals(root, traversal_type='pre_order'))
    # print(print_traversals(root, traversal_type='in_order'))
    # print(print_traversals(root, traversal_type='post_order'))

    print(bfs(root))
    """
    1. RLR  'root - left - right' - pre-order traversal
    20 - 9 - 0 - 10 - 35 - 24
    
    2. LRR - left - root - right - in-order traversal
    0 - 9 - 10 - 20 - 24 - 35
    
    3. LRR - left - right - root - post-order traversal
    0 - 10 - 9 - 24 - 35 - 20 
    
         20
        /  \
       9    35
      / \   / 
     0  10 24
     
    
    """

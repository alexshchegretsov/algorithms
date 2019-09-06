class Node:
    def __init__(self, v=None):
        self.v = v
        self.nxt = None


class Linked_List:
    def __init__(self):
        self.head = Node()

    def insert_at_end(self, v):
        new_node = v if isinstance(v, Node) else Node(v)
        cur = self.head
        while cur.nxt:
            cur = cur.nxt
        cur.nxt = new_node

    def display(self):
        tmp = []
        cur = self.head
        while cur.nxt:
            cur = cur.nxt
            tmp.append(cur.v)
        print(tmp)


def merge_lists(first_list: Linked_List, second_list: Linked_List, merged: Linked_List):
    """ 1->3->4 || 2->7->9 """
    cur_first = first_list.head.nxt
    cur_second = second_list.head.nxt
    while True:
        if not cur_first:
            merged.insert_at_end(cur_second)
            break
        if not cur_second:
            merged.insert_at_end(cur_first)
            break
        if cur_first.v < cur_second.v:
            dummy = cur_first.nxt
            cur_first.nxt = None
            merged.insert_at_end(cur_first)
            cur_first = dummy
        else:
            dummy = cur_second.nxt
            cur_second.nxt = None
            merged.insert_at_end(cur_second)
            cur_second = dummy


if __name__ == '__main__':
    a = Linked_List()
    a.insert_at_end(1)
    a.insert_at_end(3)
    a.insert_at_end(4)
    a.display()

    b = Linked_List()
    b.insert_at_end(2)
    b.insert_at_end(7)
    b.insert_at_end(9)
    b.display()

    c = Linked_List()
    merge_lists(a, b, c)
    c.display()

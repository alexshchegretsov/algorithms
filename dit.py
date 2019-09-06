class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = node()

    def length(self):
        cur = self.head
        i = 0
        while cur.next:
            i += 1
            cur = cur.next
        return i

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if 0 <= index < self.length():

            cur = self.head
            while index + 1:
                cur = cur.next
                index -= 1
            return cur.data
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = node(val)
        first = self.head.next
        new_node.next = first
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.length():
            self.addAtTail(val)
        elif 0 <= index < self.length():
            new_node = node(val)
            cur = self.head
            last = cur
            while index + 1:
                last = cur
                cur = cur.next
                index -= 1
            last.next = new_node
            new_node.next = cur

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.length():
            cur = self.head
            last = cur
            while index + 1:
                last = cur
                cur = cur.next
                index -= 1
            last.next = cur.next

    def display(self):
        elem = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elem.append(cur.data)
        print(elem)

    def del_by_value(self, value):
        cur = self.head
        last = cur
        while cur.next:
            if cur.data == value:
                last.next = cur.next
                break
            last = cur
            cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(5)
obj.addAtTail(7)
obj.addAtIndex(1, 0)
obj.del_by_value(0)
obj.display()

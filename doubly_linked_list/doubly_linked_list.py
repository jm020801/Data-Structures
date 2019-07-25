"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'[{self.value}]'

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print(self):
        if not self.head and not self.tail:
            print("Empty")
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def add_to_head(self, value):
        if self.head == None:
            new_node = ListNode(value)
            self.tail = new_node
            self.head = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length = self.length + 1

    def remove_from_head(self):
        delete_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.delete()
        self.length = self.length - 1
        return delete_value

    def add_to_tail(self, value):
        if self.tail == None:
            new_node = ListNode(value)
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length = self.length + 1

    def remove_from_tail(self):
        delete_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
        self.length = self.length - 1
        return delete_value

    def move_to_front(self, node):
        self.add_to_head(node.value)
        if self.tail == node:
            self.tail = self.tail.next
        node.delete()
        self.length = self.length - 1

    def move_to_end(self, node):
        self.add_to_tail(node.value)
        if self.head == node:
            self.head = self.head.next
        node.delete()
        self.length = self.length - 1

    def delete(self, node):
        if not self.head and not self.tail:
            return False

        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        node.delete()
        self.length = self.length - 1

    def get_max(self):
        if not self.head and not self.tail:
            return False

        current = self.head
        maximum = self.head.value
        while current:
            if current.value > maximum:
                maximum = current.value
            current = current.next
        return maximum

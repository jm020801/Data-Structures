# ------------------ Linked List Setup ----------------- #
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

    def get_next_node(self):
        return self.next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_as_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_from_head(self):
        if not self.head and not self.tail:
            return
        old_head_value = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        else:
            self.head = self.head.get_next_node()
            return old_head_value


# ------------- class Queue (using Linked List) ------------ #

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.size += 1
        self.storage.add_as_tail(item)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size

# ------------ class Queue (using Arrays/Lists) ----------- #

# class Queue:
#     def __init__(self):
#         self.size = 0
#         # what data structure should we
#         # use to store queue elements?
#         self.storage = []

#     def enqueue(self, item):
#         self.size += 1
#         self.storage.append(item)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)

#     def len(self):
#         return self.size

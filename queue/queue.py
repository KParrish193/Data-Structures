"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
    Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
    as the underlying storage structure.
    Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
    implementing a Queue? - time to process (linear)

Stretch: What if you could only use instances of your Stack class to implement the Queue?
        What would that look like? How many Stacks would you need? Try it!
"""

#  ? array, initialize as an empty list, then add/remove accordingly
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         # ? adds to end of list
#         self.storage.append(value)

#     def dequeue(self):
#         # ? means the list is empty
#         if len(self.storage) == 0:
#             return None
#         # ? removes item from first of list
#         return self.storage.pop(0)




# ? linked list iteration, initialize as LinkedList class from other file
from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        self.size -= 1
        return self.storage.remove_from_head()

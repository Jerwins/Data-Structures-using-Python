"""
Implementation of Stack Data Structure (LIFO)
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return self.items == []


myStack = Stack()

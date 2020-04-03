class Node:
    # Constructor initializes node automatically
    # Node contains data and a pointer to the next node
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    # Adding element to the top of the stack
    # Both for push & pop operation, we first check if the stack is empty first
    def push(self, data):
        if not self.head:
            self.head = Node(data)

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # Python grabage collection happens implicitly
    # Returns the removed element in the top of the stack
    def pop(self):
        if not self.head:
            return None
        nodeToBeRemoved = self.head.data
        self.head = self.head.next
        return nodeToBeRemoved

    # Traverse through the stack and display items in the stack
    def display(self):
        traverse = self.head
        while traverse != None:
            print(traverse.data, "->", end=" ")
            traverse = traverse.next


sampleStack = Stack()

# example instructions
sampleStack.push(140)
sampleStack.push(3)
sampleStack.push(49)
sampleStack.push(77)
sampleStack.display()

# Expected output: 44 -> 33 -> 22 -> 11 ->

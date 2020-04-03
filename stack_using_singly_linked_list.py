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

    # Returns the top most element in a stack
    def peek(self):
        if not self.head:
            return None
        return self.head.data


sampleStack = Stack()

# example instructions
sampleStack.push(140)
sampleStack.push(3)
sampleStack.push(49)
sampleStack.push(77)
print(sampleStack.peek(),
      "Peek element = Recently pushed to the stack / Top element in a stack ",
      end="\n")
sampleStack.display()


# Expected output:

# 77 Peek element = Recently pushed to the stack / Top element in a stack
# 77 -> 49 -> 3 -> 140 ->

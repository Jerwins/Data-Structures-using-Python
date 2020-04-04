class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        trav = self.head
        while trav.next != None:
            trav = trav.next
        trav.next = newNode

    def lengthOfSinglyList(self):
        trav = self.head
        count = 0
        while trav.next != None:
            count += 1
            trav = trav.next

        return count

    def show(self):
        trav = self.head
        #count = 0
        while trav != None:
            # print(count)
            print(trav.data, "->", end=" ")
            # print("\n")
            trav = trav.next
            #count += 1

    def get(self, index):
        if index >= self.lengthOfSinglyList():
            return "Index out of range"

        position = 0
        trav = self.head
        while trav.next != None:
            trav = trav.next
            if position == index:
                return trav.data
            position += 1

    def delete(self, index):
        if index >= self.lengthOfSinglyList():
            return "Index out of range"
        position = 0
        trav = self.head
        while trav.next != None:
            tail_node = trav
            trav = trav.next
            if position == index:
                tail_node.next = trav.next
                return "Node deleted"
            position += 1

    def insert(self, index, value):
        if index >= self.lengthOfSinglyList():
            return "Index out of range"
        elif index == self.lengthOfSinglyList():
            self.append(value)
            return "Node inserted at tail position"

        newNode = Node(value)
        position = 0
        trav = self.head
        while trav.next != None:
            tail_node = trav
            trav = trav.next
            if position == index:
                tail_node.next = newNode
                newNode.next = trav
                return "Node Added"

            position += 1


sample = singly_linked_list()

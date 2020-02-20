class Node:

    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  #Intialize next to none

class LinkedList:

    # Function to intialize LinkedList
    def __init__(self):
        self.head = None

    # Function to print LinkedList
    def printLinkedList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next 
        print()

arrLinked = LinkedList()

arrLinked.head = Node(1)
second = Node(2)
third = Node(3)

arrLinked.head.next = second
second.next = third
third.next = None

arrLinked.printLinkedList()


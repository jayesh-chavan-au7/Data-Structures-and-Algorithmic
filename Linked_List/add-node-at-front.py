class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def push(self, new_data):
        new_node = Node(new_data) #Add new node
        new_node.next = self.head #Point next to old head
        self.head = new_node #Make new node as head


arrLinkedList = LinkedList()

arrLinkedList.head = Node(100)
second = Node(200)
third = Node(300)
fourth = Node(400)

arrLinkedList.head.next = second
second.next = third
third.next = fourth
fourth.next = None

arrLinkedList.printLinkedList()

arrLinkedList.push(500)
arrLinkedList.printLinkedList()
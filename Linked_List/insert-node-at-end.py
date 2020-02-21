class Node:

    def __init__(self, data):
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

    def insertEnd(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node


arrLL = LinkedList()

arrLL.head = Node(100)
second = Node(200)
third  = Node(300)

arrLL.head.next = second
second.next = third
third.next = None

arrLL.printLinkedList()

arrLL.insertEnd(500)
arrLL.printLinkedList()


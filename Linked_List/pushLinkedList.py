class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def pushLL(self,data):
        New_data = data
        if self.head == None:
            self.head = Node(New_data)
            global prev 
            prev = self.head
            return
        New_Node = Node(New_data)
        prev.next = New_Node
        prev = New_Node

    def push(self,lenght):
        lenLL = lenght
        while lenLL != 1:
            data = int(input())
            New_data = data
            if self.head == None:
                self.head = Node(New_data)
                global prev 
                prev = self.head
                continue
            New_Node = Node(New_data)
            prev.next = New_Node
            prev = New_Node
            lenLL -= 1


arrLL = LinkedList()

arrLL.push(5)
arrLL.printLinkedList()
            
        

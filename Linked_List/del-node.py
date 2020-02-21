class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printLinked(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def delete(self,Dnode):
        if self.head == None:
            print('List is empty')
            return
        temp1 = self.head
        while temp1:
            if Dnode == self.head.data:
                self.head = self.head.next
                break
            prev = temp1
            temp1 = prev.next
            if temp1.data == Dnode:
                prev.next = temp1.next
                temp1.next = None
                break


arrLL = LinkedList()

arrLL.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

arrLL.head.next = second
second.next = third
third.next = fourth

arrLL.printLinked()
arrLL.delete(1)
arrLL.printLinked()

    
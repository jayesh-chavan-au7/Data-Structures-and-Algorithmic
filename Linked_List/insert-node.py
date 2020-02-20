class Node:

    def __init__(self, data):
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
        
    def insert(self, prevNode, new_data):
        if prevNode is None:
            print("prevNode must be in the Linked List")
            return
        new_node = Node(new_data)
        new_node.next = prevNode.next
        prevNode.next = new_node

arrLL = LinkedList()

arrLL.head = Node('A')
second = Node('B')
third = Node('C')

arrLL.head.next = second
second.next = third
third.next = None

arrLL.printLinkedList()
arrLL.insert(second, 'T')
arrLL.printLinkedList()


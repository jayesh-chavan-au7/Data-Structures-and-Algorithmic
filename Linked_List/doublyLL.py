class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:

    def __init__(self):
        self.head = None

    def push(self, data):
        New_node = Node(data)
        New_node.next = self.head

        if self.head is not None:
            self.head.prev = New_node

        self.head = New_node

    def insertAfter(self, prev_node, data):

        if self.head is not None:
            print("the given previous node cann not be Null")
            return

        New_node = Node(data)
        New_node.next = prev_node.next
        prev_node.next = New_node
        New_node.prev  = prev_node

        if New_node.next is not None:
            New_node.next.prev = New_node

    def appendDLL(self, data):
        New_node = Node(data)
        last = self.head

        New_node.next = None

        if self.head is None:
            New_node.prev = None
            self.head = New_node
            return

        while (last.next is not None):
            last = last.next

        last.next = New_node
        New_node.prev = last

    def printDLL(self, node):
        print('In forword direction')
        while(node is not None):
            print(node.data,end=" ")
            last = node
            node = node.next
        print()
        print('In reversed direction')
        while(last is not None):
            print(last.data,end=" ")
            last = last.prev
        print()

arrDLL = DoublyLL()

arrDLL.push(1)
arrDLL.push(2)
arrDLL.push(3)
arrDLL.push(4)

arrDLL.printDLL(arrDLL.head)


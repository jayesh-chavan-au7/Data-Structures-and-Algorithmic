class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLL:

    def __init__(self):
        self.head = None

    # def push(self,data):
    #     ptr1 = Node(data)
    #     temp = self.head

    #     ptr1.next = self.head

    #     if self.head is not None:
    #         while (temp.next != self.head):
    #             temp = temp.next9
    #         temp.next = ptr1
    #     else:
    #         ptr1.next = ptr1

    #     self.head = ptr1

    def push(self,data):
        New_Node = Node(data)
        if self.head == None:
            global ptr
            ptr = self.head = New_Node
        else: 
            prev = ptr
            ptr = New_Node
            prev.next = ptr
            ptr.next = self.head     

    def printCLL(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data,end=" ")
                temp = temp.next
                if (temp == self.head):
                    break
            print()

arrCLL = CircularLL()

arrCLL.push(1)
arrCLL.push(2)
arrCLL.push(3)
arrCLL.push(4)
arrCLL.push(5)
# print(arrCLL.head)
arrCLL.printCLL()
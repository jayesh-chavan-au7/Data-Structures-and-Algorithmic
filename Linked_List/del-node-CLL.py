class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLL:

    def __init__(self):
        self.head = None

    def pushCLL(self,length):
        lenCLL = length
        print('Enter elements')
        while lenCLL != 0:
            data = int(input())
            New_Node = Node(data)
            if self.head == None:
                global ptr
                ptr = self.head = New_Node
            else:
                prev = ptr
                ptr = New_Node
                prev.next = ptr
                ptr.next = self.head
            lenCLL -= 1

    def printCLL(self):
        temp = self.head
        print('CLL : ',end='')
        if temp is not None:
            while True:
                print(temp.data,end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()

    def deleteN(self, Ddata):
        temp = self.head
        while temp:
            if Ddata == self.head.data:
                temp = last = temp.next
                if last.next == self.head:
                    last.next = self.head.next
                    self.head = self.head.next
                    return
                else:
                    continue
            elif temp.data == Ddata:
                break
            elif temp.data != Ddata and temp.next == self.head:
                print('Not in list')
                return
            prev = temp
            temp = temp.next
        prev.next = temp.next 

arrCLL = CircularLL()

arrCLL.pushCLL(5)
arrCLL.printCLL()
arrCLL.deleteN(7)
arrCLL.printCLL()

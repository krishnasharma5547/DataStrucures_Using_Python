class Node:
    '''Created by krishna kant sharma B.tech 3rd year '''

    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("No element to print")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, '-->', end=" ")
            temp = temp.next
        print()

    def printListReverse(self):
        if self.head is None:
            print("No element to print")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, '-->', end=' ')
            temp = temp.pre
        print()

    def insertAtBeggining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.pre = new_node
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.pre = temp

    def insertAfterNode(self, data, node):
        if self.head is None:
            print("List is Empty")
            return
        new_node = Node(data)
        new_node.pre = node
        new_node.next = node.next
        if node.next is not None:
            node.next.pre = new_node
        node.next = new_node             # check it every time important

    def insertBeforeNode(self,data,node):
        if self.head is None:
            print('List is empty')
        new_node = Node(data)
        new_node.next = node
        new_node.pre = node.pre
        if node.pre is not None:
            node.pre.next = new_node
        else:
            self.head = new_node
        node.pre =new_node

    def deleteAtBeggining(self):
        self.head = self.head.next
        self.head.pre = None

    def deleteAtEnd(self):
        temp = self.head
        if self.head is None:
            print('List is Empty')
            return
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None

    def deleteElement(self, data):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print('Element not found')
            return
        if temp.pre is None:
            self.head = temp.next
            temp.next.pre = None
        elif temp.next is None:
            temp.pre.next = None
        else:
            temp.pre.next = temp.next
            temp.next.pre = temp.pre         # check importatnt


dll = DoublyLinkedList()
dll.insertAtBeggining(20)                   # 20
dll.insertAtBeggining(10)                   # 10 --> 20
dll.insertAtEnd(30)                         # 10 --> 20 --> 30
dll.insertAtEnd(40)                         # 10 --> 20 --> 30 --> 40
dll.insertAfterNode(25, dll.head.next)      # 10 --> 20 --> 25 --> 30 --> 40 -->
dll.insertBeforeNode(5, dll.head)           # 5  --> 10 --> 20 --> 25 --> 30 --> 40 -->
dll.insertBeforeNode(15, dll.head.next)     # 5 --> 15 --> 10 --> 20 --> 25 --> 30 --> 40 -->
dll.deleteAtBeggining()                     # 15 --> 10 --> 20 --> 25 --> 30 --> 40 -->
dll.deleteAtEnd()                           # 15 --> 10 --> 20 --> 25 --> 30 -->
dll.deleteElement(15)                       # 10 --> 20 --> 25 --> 30 -->
dll.printList()
dll.printListReverse()


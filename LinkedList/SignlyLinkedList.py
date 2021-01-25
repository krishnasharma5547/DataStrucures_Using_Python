class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insertAtBeggning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertInBetween(self, data, node_after):
        if node_after is None:
            print("Please provide valid node_after value")
            return
        new_node = Node(data)
        temp = self.head
        new_node.next = node_after.next
        node_after.next = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def deleteAtBegging(self):
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print('No element to delete')
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def deleteAnyNode(self, val):
        if self.head is None:
            print('No value to delete')
            return
        if self.head.data == val:
            self.head = self.head.next
        temp = self.head
        while temp:
            if temp.data == val:
                pre.next = temp.next
                return
            pre = temp
            temp = temp.next
        print("element not found")

    def deleteAtPosition(self, position):
        if position < 0 or position > self.listLength():
            print('Enter valid position')
            return
        if position == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        pre = self.head
        while count <= position:
            if count == position:
                pre.next = temp.next
                return
            count = count + 1
            pre = temp
            temp = temp.next

    def listLength(self):
        c = 0
        temp = self.head
        while temp:
            temp = temp.next
            c = c + 1
        return c


ll = SinglyLinkedList()
ll.deleteAtEnd()
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertInBetween(40, ll.head.next)
ll.insertAtEnd(50)
ll.insertAtBeggning(10)
ll.deleteAtEnd()
ll.deleteAnyNode(30)
ll.deleteAtPosition(2)
ll.printList()
print(ll.listLength())

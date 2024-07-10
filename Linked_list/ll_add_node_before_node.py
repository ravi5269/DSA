class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_before(self, data, value):
        if self.head is None:
            print("Linked list is Empty")
            return 
        if self.head.data == value:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        temp = self.head
        prev = None
        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.ref
        if temp is None:
            print("Node with value", value, "is not found in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = temp
            if prev is not None:
                prev.ref = new_node


ll = LinkedList()
ll.head = Node(10)
node2 = Node(20)
node3 = Node(30)
ll.head.ref = node2
node2.ref = node3

ll.add_before(15, 20)  
temp = ll.head
while temp is not None:
    print(temp.data)
    temp = temp.ref

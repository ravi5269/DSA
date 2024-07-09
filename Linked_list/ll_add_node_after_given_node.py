class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_starting(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def printlinkedlist(self):
        if self.head is None:
            print("linked is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.ref is not None:
                temp = temp.ref
            temp.ref = new_node

    def add_after(self,data,value):
        temp = self.head
        while temp is not None:
            if value == temp.data:
                break
            temp = temp.next
        
        if temp is None:
            print("Node is not found in Linkedlist")
        else:
            new_node = Node(data)
            new_node.ref = temp.ref
            
            temp.ref = new_node



obj1 = Linkedlist()
# obj1.add_starting(20)
# obj1.add_starting(200)

obj1.add_end(89)
obj1.add_after(58,89)
obj1.add_after(5,89)

obj1.printlinkedlist()

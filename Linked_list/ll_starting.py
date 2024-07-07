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
            print("linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
obj1 = Linkedlist()
obj1.add_starting(20)

obj1.add_starting(200)

obj1.add_starting(2000)

obj1.printlinkedlist()







        
# 5 july 2024
# Understanding Stack Data Structure
# A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
#  The last element added to the stack will be the first one to be removed.
#  It is analogous to a stack of plates where the last plate placed on the top is the first one to be taken off.



# Key Operations on a Stack
# Push: Add an element to the top of the stack.
# Pop: Remove the top element from the stack.
# Peek/Top: Return the top element of the stack without removing it.
# isEmpty: Check if the stack is empty.

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # Output: [10, 20, 30]
    print("Popped item:", stack.pop())  # Output: Popped item: 30
    print("Top item:", stack.peek())    # Output: Top item: 20
    print("Stack size:", stack.size())  # Output: Stack size: 2
    stack.display()  # Output: [10, 20]





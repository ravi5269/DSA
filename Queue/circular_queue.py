class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        
        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return item

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

# Example usage:
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.is_full())  # Output: True

print(cq.dequeue())  # Output: 1
print(cq.enqueue(4))  # Inserts 4 in place of 1
print(cq.peek())  # Output: 2

print(cq.dequeue())  # Output: 2
print(cq.dequeue())  # Output: 3
print(cq.dequeue())  # Output: 4
print(cq.is_empty())  # Output: True

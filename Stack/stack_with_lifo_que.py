from queue import LifoQueue

stack = LifoQueue(maxsize=4)
stack.put('x')
stack.put('y')
stack.put('z')


print("Full",stack.full())
print("Size",stack.qsize())
print(stack.get())
print(stack.get())
print(stack.get())


print("Empty",stack.empty())
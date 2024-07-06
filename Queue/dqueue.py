import collections 

q = collections.deque()
q.append(100)
q.append(200)
q.append(300)
q.append(400)

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)

print(q)
print(q.pop())
print(q.pop())
print(q.popleft())


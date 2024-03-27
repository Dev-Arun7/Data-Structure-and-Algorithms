
from queue import PriorityQueue

q = PriorityQueue()
q.put(10)
q.put(60)
q.put(40)
q.put(100)
q.put(20)

element = q.get()
print("first:", element)

element = q.get()
print("Second:", element)
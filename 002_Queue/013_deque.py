from collections import deque
my_deque  = deque()
my_deque = deque([1, 2, 3, 4])
my_deque.appendleft(0)
element = my_deque.popleft()
print(element)
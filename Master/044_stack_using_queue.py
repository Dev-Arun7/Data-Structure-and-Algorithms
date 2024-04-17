
# Program to implement a stack using
# two queue
class Stack:
	def __init__(self):
		# Two inbuilt queues
		self.q1 = []
		self.q2 = []

	def push(self, data):
		# Push data first in empty q2
		self.q2.append(data)

		# Push all the remaining
		# elements in q1 to q2.
		while (self.q1):
			self.q2.append(self.q1.pop(0))

		# swap the names of two queues
		self.q1, self.q2 = self.q2, self.q1

	def pop(self):
		# if no elements are there in q1
		if self.q1:
			return self.q1.pop(0)

	def top(self):
		if (self.q1):
			return self.q1[0]
		return None

	def size(self):
		return len(self.q1)


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("current size: ", s.size())
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())

print("current size: ", s.size())

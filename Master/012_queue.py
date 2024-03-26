from queue import Queue

# Creating an empty queue
my_queue = Queue()

my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

element = my_queue.get()  # Removes and returns the first element from the queue
print(element)


if my_queue.empty():
    print("Queue is empty")
else:
    print("Queue is not empty")

size = my_queue.qsize()

print(f"size is {size}")
 
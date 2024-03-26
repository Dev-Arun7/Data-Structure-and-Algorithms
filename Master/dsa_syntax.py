################################################################
#------------------------SYNTAXES FOR DSA----------------------#
################################################################


#--------------------------ARRY LIST--------------------------#
my_list = []
my_list.append(0)
element = my_list.pop()
my_list[i]


#---------------------------STACK------------------------------#
my_stack = []
mystack.append(element)
item = my_stack.pop()

 
#----------------------------DEQUE-----------------------------#
from collections import deque
my_deque = deque()          # Creating an empty deque
my_deque = deque([1,2,3])   # Initilizing some variables
my_deque.append(4)
my_deque.appendleft(5)
right_element = my_deque.pop()
left_element  = my_deque.popleft()
element = my_deque[i]       # Accessing an element


#----------------------------QUEUE-----------------------------#
from queue import Queue
my_queue = Queue()          # Creating an empty queue
my_queue = Queue(maxsize=3) # Queue with maximum size of 3
my_queue.put(1)             # Appending an element
element = my_queue.get()
if my_queue.empty():        # Checking if queue is empty
    print("Queue is empty") # Checking queue is full or not
if not my_queue:
    print("Stack is empty")
if my_queue.full():
    print("Queue is full")
size = my_queue.qsize()     # Check the size


#------------------------QUEUE WITH LIST-----------------------#
queue = []
queue.append(10)            # Adding an element in the right end
element = queue.pop(0)      # Removing an element from left end


#--------------------------LIFO QUEUE--------------------------#
from queue import LifoQueue
my_stack = LifoQueue()
my_stack.put(1)
element = my_stack.get()
if my_stack.empty():
    print("stack is empty")
size = my_stack.qsize()
my_stack.queue.clear()      # Clear the stack


#--------------------------PRIORITY QUEUE------------------------#
# Tuple method
q = []
q.append(3,'Anila')
q.sort(reverse = True)
q.pop(0)

 

    
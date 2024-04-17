# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head is None

#     def push(self, data):
#         new_node = Node(data)
#         if self.is_empty():
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node
    
#     def pop(self):
#         if self.is_empty():
#             return None
#         else:
#             temp = self.head
#             self.head = temp.next
#             temp.next = None
#             return temp.data


# s = Stack()
# print(s.pop())
# s.push(10)
# s.pop()







# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.front = self.rear = None

#     def is_empty(self):
#         return self.front is None
    
#     def enque(self, data):
#         new_node = Node(data)
#         if self.is_empty():
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node


#     def deque(self):
#         if self.is_empty():
#             return None
#         else:
#             temp = self.front
#             self.front =temp.next
#             if self.front == None:
#                 self.rear = None
#             return temp.data


# q = Queue()
# print(q.deque())
# q.enque(10)
# print(q.deque())



 

 # Stack using Queue
 
# class Stack:
#     def __init__(self):
#         self.q1 = []
#         self.q2 = []

#     def push(self, data):
#         self.q2.append(data)

#         while self.q1:
#             self.q2.append(self.q1.pop(0))

#         self.q1, self.q2 = self.q2, self.q1

#     def pop(self):
#         if not self.q1:
#             return None
#         else:
#             return self.q1.pop(0)




# # Queue

# class Node:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def enque(self, data):
#         self.s1.append(data)

#     def deque(self):
#         if len(self.s1) == 0 and len(self.s2) == 0:
#             return None
#         elif len(self.s2) == 0 and len(self.s1) > 0:
#             while len(self.s1):
#                 self.s2.append(self.s1.pop())

#             return self.s2.pop()
#         else:
#             return self.s2.pop()
    




















# def sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr



































# def sort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         pivot = nums.pop()
#         lower = []
#         higher = []

#         for num in nums:
#             if num < pivot:
#                 lower.append(num)
#             else:
#                 higher.append(num)

#         return sort(lower) + [pivot] + sort(higher)










# new comments are added





# def sort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]

#         # Recursion
#         sort(left)
#         sort(right)

#         # Merge
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 k += 1
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#                 k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

#     return nums
            




























def sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Recursion
        sort(left)
        sort(right)

        # Merge
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                k += 1

            else:
                nums[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return nums
















l = int(input("Lenght: "))
print("Enter elements: ")
arr = [int(input()) for i in range(l)]
result = sort(arr)
print(result)
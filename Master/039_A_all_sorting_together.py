# Buble sort
def B_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Insertion sort
def I_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j] < nums[j-1] and j > 0:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

# Selection sort
def S_sort(nums):
    for i in range(len(nums)):
        current = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[current]:
                current = j
        nums[i], nums[current] = nums[current], nums[i]
    return nums

# Quick sort
def Q_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums.pop()
        lower = []
        higher = []
        for num in nums:
            if num < pivot:
                lower.append(num)
            else:
                higher.append(num)
        return sort(lower) + [pivot] + sort(higher)

# Merge sort
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

        # Merging
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Adding remaining elements
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums



l = int(input("Length: "))
nums = [int(input()) for i in range(l)]
print("List: ",nums)

# Call any sorting method here
result = sort(nums)
print("sorted list: ", result)

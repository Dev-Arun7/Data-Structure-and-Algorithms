def add(nums):
    if not nums:
        return 0
    else: 
        return nums[0] + add(nums[1:])


numbers = [1, 2, 3, 4, 5]
result = add(numbers)
print("Sum:", result)

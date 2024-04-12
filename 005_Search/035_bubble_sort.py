
# Bubble sort
def sort(nums):
    for i in range(len(nums)- 1):
        # Last i elements are already in place
        for j in range(len(nums) - i - 1): 
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


nums = [5, 3, 9, 0, 12, 1, 6]
result = sort(nums)
print(nums)
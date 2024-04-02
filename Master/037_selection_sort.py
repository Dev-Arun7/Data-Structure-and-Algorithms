# Selection sort
def sort(nums):
    for i in range(len(nums) - 1):
        current = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[current]:
                current = j
        nums[i], nums[current] = nums[current], nums[i]
    return nums


l = int(input("Length: "))
print("Enter the elements: ")
nums = [int(input()) for i in range(l)]
result = sort(nums)
print(nums)


# Insertion sort
def sort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j] < nums[j - 1] and j > 0:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums



l = int(input("Lenght: "))
print("Ente the elements: ")
nums = [ int(input()) for i in range(l)]
result = sort(nums)
print(result) 





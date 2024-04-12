
# Quick sort
def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop() # Popping last number
        lower = []
        higher = []

        for num in nums:
            if num > pivot:
                higher.append(num)
            else:
                lower.append(num)
    return quick_sort(lower) + [pivot] + quick_sort(higher)



l = int(input("Lenght: "))
print("Enter elements: ")
nums = [int(input()) for i in range(l)]
result = quick_sort(nums)
print(result)

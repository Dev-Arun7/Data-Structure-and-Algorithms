def b_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def in_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j] < nums[j-1] and j > 0:
            nums[j], nums[j-1 ] = nums[j - 1], nums[j]
            j -= 1
    return nums


def s_sort(nums):
    for i in range(len(nums) - 1):
        current = i
        for j in range(i+1, len(nums)):
            if nums[current] > nums[j]:
                current = j
        nums[i], nums[current] = nums[current], nums[i]
    return nums





l = int(input("Lenght: "))
nums = [int(input()) for i in range(l)]
result = s_sort(nums)
print(result)


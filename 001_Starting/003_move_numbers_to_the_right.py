def move(nums, target):
    l = len(nums)
    j = l-1
    i = 0
    while i <= j:
        if nums[i] == target:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    return nums

    

nums = [6, 5, 6, 7, 2, 8, 6, 10]
target = 6
result = move(nums, target)
print(result)


# In the corrected function, we use a while loop to iterate through the list nums. Inside the loop, we perform constant-time operations such as comparisons and swapping elements. Here's a breakdown of the time complexity:

#     The while loop iterates through the list at most n times, where n is the length of the list nums. This is because i starts from 0 and j starts from len(nums) - 1, and they converge towards the center of the list.
#     Inside the loop, most operations are constant-time, including comparisons and element swaps.

# Therefore, the time complexity of the move(nums, target) function is O(n), where n is the length of the list nums.

# In terms of space complexity, the function uses only a constant amount of extra space for variables like l, i, and j, so the space complexity is O(1), which means it's constant relative to the size of the input list.
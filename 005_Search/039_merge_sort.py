
# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:  # Base case for recursion
        return

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursion
    merge_sort(left_arr)
    merge_sort(right_arr)

    # Merge
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Appending remaining values if there
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


# Test the merge sort function
l = int(input("Length: "))
nums = [int(input()) for i in range(l)]
merge_sort(nums)
print(nums)


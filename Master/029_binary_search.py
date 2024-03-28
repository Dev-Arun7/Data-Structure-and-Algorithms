
# Binary search
def search(nums, key):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == key:
            print(f"{key} is found at {mid}")
            return
        elif key < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print("Search not found...!")

num = int(input("Length: "))
nums = [int(input()) for i in range(num)]
nums.sort()
key = int(input("Enter the key: "))
search(nums, key)

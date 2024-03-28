
# Leaniear serach program
def search(key, nums):
    for i, num in enumerate(nums):
        if key == num:
            print(f"{num} is found at the index {i}")
            break
    else:
        print("Search not found")


num = int(input("Length: "))
nums = [int(input()) for i in range(num)]
key = int(input("Enter the key: "))
search(key, nums)

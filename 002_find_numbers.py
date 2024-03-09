import time

def find_nums(arr, target):
    s_time = time.time()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                e_time = (time.time() - s_time) * 1000  # Convert seconds to milliseconds
                print(f"Total time is: {e_time} milliseconds")
                return [arr[i], arr[j]]

arr = [5, 6, 4, 3, 2, 1]
target = 10

result = find_nums(arr, target)
print(result)

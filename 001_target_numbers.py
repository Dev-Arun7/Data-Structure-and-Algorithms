def find_nums(arr, target):
    my_set = set()
    for i in arr:
        digit = i
        match = target - digit
        if match in my_set:
            return [i, match]
        else:
            my_set.add(i)




arr = [5, 6, 4, 3, 2, 1]
target = 10

result = find_nums(arr, target)
print(result)
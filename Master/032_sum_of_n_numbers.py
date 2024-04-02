# sum of n numbers
def add(n):
    if n < 1:
        return 0
    else:
        return n + add(n - 1)

result = add(5)
print(result)


# Reverse a string using recursion
def reverse(s):
    if not s:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = "hello"
result = reverse(s)
print(result)

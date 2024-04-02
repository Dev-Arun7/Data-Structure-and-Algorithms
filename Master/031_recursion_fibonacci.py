
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


result = fibonacci(6)
print(result)



# def Fibonacci(n):
# 	if n == 1:
# 		return 0
# 	# Second Fibonacci number is 1
# 	elif n == 2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1)+Fibonacci(n-2)

# # Driver Program

# print(Fibonacci(1))




data = {1 : "Arun", 2  : "Akhil", 3 : "Sujatha"}
print(data)
print(data[2])

result = data.get(4)
print(result)


print(data.get(1, 'Not found'))
print(data.get(5, 'Not found'))



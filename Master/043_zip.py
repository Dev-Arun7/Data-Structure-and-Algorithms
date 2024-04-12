key = ['Arun', 'Akhil', 'Sujatha',]
values = ['Pyhthon', 'C', 'Java']

data = dict(zip(key, values))
print(data)

data['Manu'] = 'Go'
del data['Arun']
print(data)


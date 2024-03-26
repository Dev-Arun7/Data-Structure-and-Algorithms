
q = []
q.append((2, 'Akhil'))
q.append((1, 'Anila'))
q.append((5, 'Arun'))
q.append((3, 'Balakrishnan'))
q.append((7, 'Sujatha'))
q.append((9, 'Gayathri'))

q.sort(reverse = True)
print(q.pop(0))
print(q)

q.sort()
print(q.pop(0))
print(q)

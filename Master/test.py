from collections import defaultdict

count = defaultdict(int)

print(count)
count['a'] += 1

print(count)
if 'c' in count:
    print("a is present")
else:
    count['b']

print(count) 
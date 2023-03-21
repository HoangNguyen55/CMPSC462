dict1 = {'a': 10, 'b': 20, 'c': 30, 'd':20}
print(f"{dict1 = }")
dict1['a'] = 11

i = []
j = []

for k, v in dict1.items():
    if not v in i:
        i.append(v)
    else:
        j.append(k)

for k in j:
    dict1.pop(k)

print(f"{dict1 = }")
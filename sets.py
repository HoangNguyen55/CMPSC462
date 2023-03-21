# set1 = {1, 2 , 3}
# print(set1)
# set2 = {1, 2 , 3, "hello world"}
# print(set2)
# set3 = set([1, 2, 3])
# print(set3)

# for each in set("hello world"):
#     print(each)

# set4 = {1,2,3}
# print(set4)
# set4.add(5)
# print(set4)
# set4.update([2, 3, 4, 6])
# print(set4)
# set4.add((1, 2, 8))
# print(set4)
# set4.update(['a', 'b'], ('a', 'b'))
# print(set4)

# set1 = {1, 3, 4, 5, 6}
# print(set1)
# set1.discard(4)
# print(set1)
# set1.remove(6)
# print(set1)
# set1.discard(2)
# print(set1)

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A ^ B)
# A.symmetric_difference(B)
# print(B ^ A)
# B.symmetric_difference(A)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A.isdisjoint(B))
print(A.difference(B))
print(A | B)
#A.add(3)

def a():
    return {"hello": "world"} | {"what": "the"}

print(a())

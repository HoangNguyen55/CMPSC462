i = input("put in 1st sets of comma-separated values: ")
i2 = input("put in 2nd sets of comma-separated values: ")

set1 = set(i.split(","))
set2 = set(i2.split(","))

print(f"{set1.issubset(set2) = }")
print(f"{set2.issubset(set1) = }")

print(f"{set1.issuperset(set2) = }")
print(f"{set2.issuperset(set1) = }")

print(f"{set1.union(set2) = }")
print(f"{set1.intersection(set2) = }")
print(f"{set1.difference(set2) = }")

def is_sorted(arg):
    last = arg[0]
    for i in arg:  
        if i >= last:
            last = i
        else:
            return False
    return True


print(f"{is_sorted([1, 2, 2]) = }")
print(f"{is_sorted(['b', 'a']) = }")

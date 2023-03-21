def max_val(arr):
    if len(arr) == 1:
        return arr[0]
    temp = max_val(arr[1:])
    if arr[0] > temp:
        return arr[0]
    else:
        return temp

a = [2, 5, 1, 7, 1, 2]

print(f"{max_val(a) = }")

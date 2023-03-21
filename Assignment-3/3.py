def sum(num):
    if num % 2 != 0:
        num -= 1
    if num == 2:
        return 2
    if num <= 0:
        return 0

    return num + sum(num - 2)

print(f"{sum(4) = }")

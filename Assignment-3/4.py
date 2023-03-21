def pow(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1

    return a * pow(a, b-1)


print(f"{pow(2, 6) = }")
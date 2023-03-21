def combine_dict(d1: dict, d2: dict):
    re = {}
    keys = list(d1.keys())
    keys.extend(d2.keys())

    for k in keys:
        if d1.get(k) and d2.get(k):
            re[k] = d1[k] + d2[k]
        elif d1.get(k):
            re[k] = d1[k]
        else:
            re[k] = d2[k]
            
    return re

d1 = {'x': 100, 'y': 200, 'm':100}
d2 = {'x': 200, 'n': 100, 'y':200}

print(combine_dict(d1, d2))
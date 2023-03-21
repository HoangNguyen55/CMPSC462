d1 = {'x': 10, 'y': 20, 'm': 10}
d2 = {'x': 20, 'n': 10, 'y': 10}

def a(d1, d2):
    d3 = {}
    for i in list(d1.keys() & d2.keys()):
        d3[i] = d1[i] + d2[i]
    
    return d2 | d1 | d3

def b(l):
    return list(set(l))

L = [2, 4, 2, 6, 4, 7, 8]
print(b(L))


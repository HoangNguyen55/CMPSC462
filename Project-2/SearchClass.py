from time import perf_counter

def performance_counter_decorator(func):
    def count(*args, **kwargs):
        start = perf_counter()
        re = func(*args, **kwargs)
        stop = perf_counter()
        return (stop - start, re)

    return count

# Wikipedia contributors. (2022, August 8). Linear search. Wikipedia. Retrieved September 27, 2022, from https://en.wikipedia.org/wiki/Linear_search
@performance_counter_decorator
def linear_search(array, item):
    for j, i in enumerate(array):
        if i == item:
            return j
    return -1

# Wikipedia contributors. (2022b, September 16). Binary search algorithm. Wikipedia. Retrieved September 27, 2022, from https://en.wikipedia.org/wiki/Binary_search_algorithm
@performance_counter_decorator
def binary_search(array, item):
    right = len(array)
    left = 0
    while left <= right:
        index = (left + right) // 2
        if array[index] > item:
            right = index
        elif array[index] < item:
            left = index
        else:
            return index

    return -1

@performance_counter_decorator
def max_search(array):
    temp = array[0]
    for i in array:
        if i > temp:
            temp = i

    return temp

@performance_counter_decorator
def min_search(array):
    temp = array[0]
    for i in array:
        if i < temp:
            temp = i

    return temp

@performance_counter_decorator
def distinct_search(array):
    temp = []
    dupes = []
    for i in array:
        if i in temp:
            dupes.append(i)
        else:
            temp.append(i)
    
    return (bool(len(dupes)), dupes)
from SearchClass import performance_counter_decorator

#GeeksforGeeks. (2022, September 1). Bubble Sort Algorithm. Retrieved September 27, 2022, from https://www.geeksforgeeks.org/bubble-sort/
@performance_counter_decorator
def bubble_sort(array:list):
    arr = array.copy()
    length = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if arr[i-1] > arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
                swapped = True

    return arr

@performance_counter_decorator
#Wikipedia contributors. (2022d, September 25). Insertion sort. Wikipedia. Retrieved September 27, 2022, from https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(array:list):
    arr = array.copy()
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
        i += 1

    return arr

#Wikipedia contributors. (2022d, September 25). Selection sort. Wikipedia. Retrieved September 27, 2022, from https://en.wikipedia.org/wiki/Selection_sort
@performance_counter_decorator
def selection_sort(array:list):
    temp = []
    arr = array.copy()
    while len(temp) < len(array):
        min = (arr[0], 0)
        for j, i in enumerate(arr):
            if i < min[0]:
                min = (i, j)
        temp.append(min[0])
        arr.pop(min[1])

    return temp

# Wikipedia contributors. (2022b, September 10). Merge sort. Wikipedia. Retrieved September 27, 2022, from https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
def _merge_sort(array):
    if len(array) <= 1:
        return array

    left: list = array[:len(array)//2]
    right = array[len(array)//2:]

    left = _merge_sort(left)
    right = _merge_sort(right)
    
    temp = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            temp.append(left[0])
            left = left[1:]
        else:
            temp.append(right[0])
            right = right[1:]

    while len(left):
        temp.append(left.pop(0))
    while len(right):
        temp.append(right.pop(0))

    return temp

@performance_counter_decorator
def merge_sort(*args, **kwargs):
    return _merge_sort(*args, **kwargs)
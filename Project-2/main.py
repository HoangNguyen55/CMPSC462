from random import randint
from SearchClass import *
from SortingClass import *

def fill_random(max):
    temp = []
    for _ in range(0, max):
        temp.append(randint(1, 1000))
    return temp

def search_sort(max):
    pool = fill_random(max)
    target = randint(1, 1000)
    result = {}
    result['target'] = target
    result['linear'] = linear_search(pool, target)
    _, sorted_pool = merge_sort(pool)
    result['binary']  = binary_search(sorted_pool, target)
    result['max'] = max_search(pool)
    result['min'] = min_search(pool)
    result['distinct'] = distinct_search(pool)

    result['selection'] = selection_sort(pool)
    result['insertion'] = insertion_sort(pool)
    result['bubble'] = bubble_sort(pool)
    result['merge'] = merge_sort(pool)
    
    return result

time_linear = 0
time_binary = 0
time_max = 0
time_min = 0
time_distinct = 0
time_selection = 0
time_insertion = 0
time_bubble = 0
time_merge = 0
for _ in range(3):
    result = search_sort(10_000)
    target = result['target']
    print("\nSEARCHING\n")
    time, index = result['linear']
    time_linear += time
    print(f"linear_search(pool, {target = }): {time = } | {index = }")
    time, index = result['binary']
    time_binary += time
    print(f"binary_search(sorted_pool, {target = }): {time = } | {index = }")
    time, max = result['max']
    time_max += time
    print(f"max_search(pool): {time = } | {max = }")
    time, min = result['min']
    time_min += time
    print(f"min_search(pool): {time = } | {min = }")
    time, (is_distinct, dupes) = result['distinct']
    time_distinct += time
    print(f"distinct_search(pool): {time = } | {is_distinct = } | amount of dupes = {len(dupes)}")
    print("\nSORTING\n")
    time, sort = result['selection']
    time_selection += time
    print(f"selection_sort(pool): {time = }")
    time, _ = result['insertion']
    time_insertion += time
    print(f"insertion_sort(pool): {time = }")
    time, _ = result['bubble']
    time_bubble += time
    print(f"bubble_sort(pool): {time = }")
    time, _ = result['merge']
    time_merge += time
    print(f"merge_sort(pool): {time = }")


print(f"""
Final Tabulate Result:
time_linear = {time_linear/3}
time_binary = {time_binary/3}
time_max = {time_max/3}
time_min = {time_min/3}
time_distinct = {time_distinct/3}
time_selection = {time_selection/3}
time_insertion = {time_insertion/3}
time_bubble = {time_bubble/3}
time_merge = {time_merge/3}
""")
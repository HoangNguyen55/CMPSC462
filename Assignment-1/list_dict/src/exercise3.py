def remove_keys(dictionary: dict, key_list):
    re = dictionary
    for k in key_list:
        re.pop(k)
    return re

dict1 = {'a': 1, 'b': 2 , 'c': 3, 'd': 4, 'e': 5}
rmkey = ['b', 'd', 'e']

print(f"{dict1 = }")

dict2 = remove_keys(dict1, rmkey)

print(f"{dict2 = }")
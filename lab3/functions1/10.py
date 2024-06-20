"""
Write a Python function that takes a list and 
returns a new list with unique elements of the 
first list. Note: don't use collection set.
"""
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 3, 2, 4, 5, 6, 5, 7, 8, 9, 1]
result = unique_elements(original_list)
print(original_list)
print(result)
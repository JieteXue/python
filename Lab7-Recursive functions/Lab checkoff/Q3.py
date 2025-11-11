def deep_copy_list(original):
    if not isinstance(original, list):
        return original
    
    copy = []
    for item in original:
        if isinstance(item, list):
            copy.append(deep_copy_list(item))
        else:
            copy.append(item)
    return copy


original_list = [1, [2, 3], [4, [5, 6]]]
copied_list = deep_copy_list(original_list)

print("Original List:", original_list)
print("Copied List:", copied_list)

original_list[0] = 10
original_list[1][0] = 20
original_list[2][1][0] = 30

print("Original List after modifications:", original_list)
print("Copied List after modifications:", copied_list)
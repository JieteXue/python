def unzip(pairs):
    list1 = []
    list2 = []
    for i in range(len(pairs)):
        list1.append(pairs[i][0])
        list2.append(pairs[i][1])
    return list1, list2

print(unzip([(1, 'A'), (2, 'B')]))  
print(unzip([(1, 'A'), (2, '')]))  
print(unzip([]))  
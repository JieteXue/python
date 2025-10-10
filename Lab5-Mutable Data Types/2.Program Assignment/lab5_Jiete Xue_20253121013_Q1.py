def merge_sorted_lists(list1, list2):
    list=sorted(list1+list2)
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            list.remove(list[i])
    return list
print(merge_sorted_lists([1,3,5], [2,4,6]))
print(merge_sorted_lists([1,3,5], [])) 
print(merge_sorted_lists([10], [2,4,6]))
    
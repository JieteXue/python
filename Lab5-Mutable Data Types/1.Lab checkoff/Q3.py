def target_sum_pair(list, target):
    a=sorted(list)
    true=[]
    i=0
    j=len(a)-1
    while i<j:
        if a[i]+a[j]==target:
            true.append( [a[i],a[j]])
            i=i+1
        elif a[i]+a[j]>target:
            j=j-1
        else:
            i=i+1
    return true
print(target_sum_pair([1,2,5,4,7],9))
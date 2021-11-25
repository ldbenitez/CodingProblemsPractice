def solution(a):

    n_counter = [0 for x in range(100000)]
    dup_number = -1
    for index in range(len(a)): 
        if n_counter[a[index]-1]==0:
            n_counter[a[index]-1]=1
        else:
            dup_number = a[index]
            break
    return dup_number
def comman_in_list(l1,l2):
    comman = []
    for i in l1 :
        if i in l2 :
            comman.append(i)
    return comman
print(comman_in_list([1,2,3,4,5,6],[4,5,6,7,8,9,2]))
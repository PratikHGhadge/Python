def sublist_counter(l):
    count = 0
    for i in l :
        if type(i) == list :
            count += 1
    return count
mix = [1,2,3,[3,4,4],[2,3],[0]]

print(sublist_counter(mix))
def filter_odd_even_num(l):
    odd =  []
    even = []
    for i in l :
        if i%2 == 0 :
            even.append(i)
        else:
            odd.append(i)
        output = [odd,even]
    return output

print(filter_odd_even_num([1,42,4,6,78,8,6,4,22]))
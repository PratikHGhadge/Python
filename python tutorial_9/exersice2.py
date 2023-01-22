# example
# input = ['true','false','0.1','1','3']
# output =

def num_to_string(l):
    return [str(i) for i in l if(type(i) == int  or type(i) == float)]

print(num_to_string(['true','false',0.1,1,3]))






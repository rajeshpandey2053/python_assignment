from functools import reduce
def reduce_function(a, b):
    
    a.update(b)
    return a
    

def take_input():
    dict = {}
    a = int(input("enter the no of key value pairs"))
    for _ in range(a):
        dict.update({input("enter key") : input("enter value")})
    return dict


no_of_dict = int(input("Enter the number of dictionary: "))
iterable_list= []
for _ in range(no_of_dict):
    iterable_list.append(take_input())

result = reduce(reduce_function,iterable_list)
print(result)

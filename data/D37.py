from functools import reduce
a_dict = {"a":1, "b":2, "c": 3}
values = a_dict.values()



total = reduce(lambda x,y: x*y ,values)

print(total)
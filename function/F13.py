def sort_func(li):
    li.sort(key= lambda x: x[1])
    print(li)

tuple_var = [('gopal',15), ('shyam',22), ('hari', 8)]
sort_func(tuple_var)

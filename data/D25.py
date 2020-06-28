mylist = [{}, {},{}]
mylist1 = [{1}, {34}, {}]

def empty_func(li):
    all_true = False
    for diction in li:
        if bool(diction):
            all_true = True

    if all_true:
        print('not empty')
    else:
        print("all are empty")
        

empty_func(mylist1)
empty_func(mylist)
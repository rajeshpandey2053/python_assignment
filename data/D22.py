def remove_dup(x):
    return list(dict.fromkeys(x))

no_of_integers = int(input('enter the no of items in list: '))
input_list = []
for _ in range(no_of_integers):
    input_list.append (input("Enter item: "))


result = remove_dup(input_list)
print(result)
def last_int(integer):
    return integer[-1]

no_of_integers = int(input('enter the no of tuples in list: '))
input_list = []
for _ in range(no_of_integers):
    input_list.append(input("Enter tuples: "))
result = sorted(input_list, key = last_int)
print(result)
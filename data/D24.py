no_of_integers = int(input('enter the no of items in list: '))
input_list = []
for _ in range(no_of_integers):
    input_list.append(input("Enter item: "))

new_list = input_list.copy()
print("The copied list is: ", new_list)
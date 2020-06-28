print("Enter the list: ")
no_of_integers = int(input('enter the no of items in list: '))
input_list = []
for _ in range(no_of_integers):
    input_list.append(input("Enter item: "))
input_string = input("Enter the string: ")

result = []
for li in input_list:
    result.append(input_string + li)

print(result)
no_of_integers = int(input('enter the no of items in list: '))
input_list = []
for _ in range(no_of_integers):
    input_list.append(int(input("Enter item: ")))

result = min(input_list)
print(result)
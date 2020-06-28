def take_input():
    print("Enter the list: ")
    no_of_integers = int(input('enter the no of items in list: '))
    input_list = []
    for _ in range(no_of_integers):
        input_list.append(input("Enter item: "))
    return input_list

a = take_input()
b = take_input()
a.pop()
a.extend(b)
print(a)
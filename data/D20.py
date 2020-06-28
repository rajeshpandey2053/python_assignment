no_of_integers = int(input('enter the no of strings in list: '))
input_list = []
for _ in range(no_of_integers):
    input_list.append(input("Enter strings: "))

count_result = 0
for strings in input_list:
    if (len(strings)>=2) and (strings[0] == strings[-1]):
        count_result = count_result +1
print(count_result)

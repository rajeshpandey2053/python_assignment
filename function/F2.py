def sum_func(func_list):
    return sum(func_list)

input_list = []
no = int(input("Enter how many numbers in list: "))
for _ in range(no):
    input_list.append(int(input("Enter item: ")))

print("The sum of list is: ", sum_func(input_list))
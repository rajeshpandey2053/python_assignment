from functools import reduce

def multiply(a,b):
    return a*b

input_list = []
no = int(input("Enter how many numbers in list: "))
for _ in range(no):
    input_list.append(int(input("Enter item: ")))

result = reduce(multiply,input_list)
print("The multiplication of alll numbers in list is: ", result)
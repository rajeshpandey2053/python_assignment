def even_num(li):
    result = []
    for i in li:
        if i % 2 ==0:
            result.append(i)
    print("Even numbers are: ",result)

input_list = []
no = int(input("Enter how many numbers in list: "))
for _ in range(no):
    input_list.append(int(input("Enter item: ")))

even_num(input_list)

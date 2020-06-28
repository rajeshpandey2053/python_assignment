def unique_list(l):
    se = set(l)
    return list(se)
   
input_list = []
no = int(input("Enter how many numbers in list: "))
for _ in range(no):
    input_list.append(int(input("Enter item: ")))

print("The sum of list is: ", unique_list(input_list))
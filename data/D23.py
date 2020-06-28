input_list = []
flag = True
while(flag):
    y_n_var = input('Do you want to enter data: say (y/n) ')
    if y_n_var == 'y':
        input_list.append(input("enter item: "))

    elif y_n_var == 'n':
        flag = False
    else:
        print('Enter the required (y/n): ')

if bool(input_list):
    print("list is not empty")
else:
    print("list is empty")

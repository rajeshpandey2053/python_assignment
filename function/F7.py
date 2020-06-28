def calc(string):
    lower,upper = 0,0
    for char in string:
        if (char>='a' and char<='z'):
            lower+=1
        if (char>='A' and char<='Z'):
            upper+=1
    return upper,lower


input_string = input("Enter the string: ")
no_upper , no_lower = calc(input_string)
print("The number of upper cases are: ",no_upper,'\n','The number of lower cases are: ',no_lower)


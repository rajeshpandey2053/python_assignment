input_string = input('Enter the two strings as comma separated: ')
splitted_string = input_string.split(',')
temp_var = splitted_string[0]
middle_int = len(temp_var)//2
result = temp_var[:2] + splitted_string[1] + temp_var[2:]
print(result)
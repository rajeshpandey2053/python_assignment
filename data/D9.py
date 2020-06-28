string = input('Enter the string: ')
mid_part = string[1:-1] 
result = string[-1] + mid_part + string[0]
print(result)
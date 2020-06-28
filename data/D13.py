string = input('Enter the string: ')
temp = string.split(",")
temp.sort()
print(','.join(temp))
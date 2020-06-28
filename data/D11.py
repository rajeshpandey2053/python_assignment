string = input('Enter the string: ')
result = {}
temp = string.split(' ')
for words in temp:
    if words not in result.keys():
        result[words] = 1
    else:
        result[words] = result[words] + 1
print(result)
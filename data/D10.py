string = input('Enter the string: ')
result = []
for i in range(0,len(string),2):
    result.append(string[i])
print("".join(result))
inputchar = input()

temp = inputchar.replace(inputchar[0],'$')
result = temp.replace('$',inputchar[0],1)

print(result)

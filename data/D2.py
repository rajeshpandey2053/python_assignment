inputchar = input()
if len(inputchar)>=2:
    result = inputchar[:2] + inputchar[-2:]
else:
    result = ''

print(result)

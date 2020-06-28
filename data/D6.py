inputstr = input("Enter the string: ")
findnot = inputstr.find('not')
findpoor = inputstr.find('poor')
if findpoor>findnot and findnot>0 and findpoor>0:
    substring = inputstr[findnot:findpoor+4]
    result = inputstr.replace(substring, 'good')
else:
    result = inputstr

print(result)
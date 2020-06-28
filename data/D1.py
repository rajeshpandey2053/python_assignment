inputchar = input()
mydict = {}
for char in inputchar:
    if char not in mydict.keys():
        mydict[char] = 1
    else:
        mydict[char] = mydict[char] + 1
print(mydict)

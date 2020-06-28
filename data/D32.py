dicttionary = {}
a = int(input("enter the no of key value pairs"))
for i in range(1,a+1):
    
    dicttionary.update({i : i*i})
print(dicttionary)
string = input("Enter the string: ")
char = input("Enter the character: ")


func = lambda str,ch: str.startswith(ch)
print(func(string,char))
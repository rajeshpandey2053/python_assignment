def reversed(in_string):
    reversed_string = ''
    for i in range(len(in_string)):
        reversed_string = reversed_string + in_string[len(in_string)-i-1]
    return reversed_string
    
    
input_string = input("Enter the string to be reversed: ")

print("The reversed string is: ", reversed(input_string))
nth_index = int(input('Enter the nth index: '))
string = input('Enter the non-empty string: ')
first_part = string[:nth_index]
second_part = string[nth_index+1:]
print(first_part + second_part)

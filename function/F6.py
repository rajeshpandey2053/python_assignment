def range_func(first_range, second_range, num):
    if num in [i for i in range(first_range,second_range+1)]:
        print("yes number is in range ")
    else:
        print("not in range")

first_r = int(input("Enter the first range: "))
second_r = int(input("Enter the second range: "))
number = int(input("Enter the number: "))
range_func(first_r,second_r,number)
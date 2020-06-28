num = int(input("Enter the num to add 15: "))
fun = lambda x: x+15
print("The sum is : ", fun(num))
num1 = int(input("Enter the num x to multiply : "))
num2 = int(input("Enter the num y to multiply: "))
mul = lambda num1,num2: num1*num2
print("The mul is: ", mul(num1,num2))
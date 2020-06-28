car = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
}

key = input('enter the key: ')
value = input('enter the value: ')
car.update({key : value})

print(car)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
search = input("enter the key to be searched: ")

if (car.get(search)):

	print("value found: ",car[search])
else:
	print("not found")
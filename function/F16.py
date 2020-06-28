ages = [5, 12, 17, 18, 24, 32]

square= map(lambda x: x*x, ages)
cube = map(lambda x: x*x*x, ages)

print("The squares are : ", list(square))
print("The cubes are: ", list(cube))
ages = [5, 12, 17, 18, 24, 32]

adults = filter(lambda x: x>=18, ages)

for x in adults:
  print(x)
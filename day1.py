# The Tyranny of the Rocket Equation

fin = open("input_day1.txt", "r")
lines = fin.readlines()

total = 0
for line in lines:
  el = line.split()
  total += int(el[0]) // 3 - 2

print(total)

# part 2

total = 0
for line in lines:
  el = line.split()
  x = int(el[0])
  x = x // 3 - 2
  while x > 0:
    total += x
    x = x // 3 - 2

print(total)

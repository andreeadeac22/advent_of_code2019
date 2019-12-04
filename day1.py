# The Tyranny of the Rocket Equation

fin = open("day1_input.txt", "r")
lines = fin.readlines()

total = 0
for line in lines:
  el = line.split()
  if len(el) > 0:  
    total += int(el[0]) // 3 - 2

print(total)

# part 2

total = 0
for line in lines:
  el = line.split()
  if len(el) > 0:
    x = int(el[0])
    x = x // 3 - 2
    while x > 0:
      total += x
      x = x // 3 - 2

print(total)

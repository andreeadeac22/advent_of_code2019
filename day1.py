# The Tyranny of the Rocket Equation

fin = open("day1_input.txt", "r")
lines = fin.readlines()

total = 0
for line in lines:
  el = line.split()
  if len(el) > 0:  
    total += int(el[0]) // 3 - 2

print(total)

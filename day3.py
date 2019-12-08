file = open("input_day3.txt", "r") 
lines = file.readlines()
arr1 = lines[0].split(",")
arr2 = lines[1].split(",")

def add_positions(arr, pos, dir, len):
  for i in range(len):
    if dir == 'R':
      pos = (pos[0] + 1, pos[1]) 
    if dir == 'U':
      pos= (pos[0], pos[1] + 1)
    if dir == 'L':
      pos = (pos[0] - 1, pos[1])
    if dir == 'D':
      pos = (pos[0], pos[1] - 1)
    arr.append(pos)
  return arr, pos


positions1 = [(0,0)]
pos1 = (0,0)
pos2 = (0,0)
positions2 = [(0,0)]
# R x+, U y+, L x-, D y-
for el in arr1:
  dir = el[0]
  length = int(el[1:])
  positions1, pos1 = add_positions(positions1, pos1, dir, length)

for el in arr2:
  dir = el[0]
  length = int(el[1:])
  positions2, pos2 = add_positions(positions2, pos2, dir, length)

positions1.sort()
positions2.sort()

def inters(p1, p2):
  i = 0 
  j = 0
  min = 2147483647
  while i<len(p1) and j<len(p2):
    if p1[i][0] < p2[j][0] or (p1[i][0] == p2[j][0] and p1[i][1] < p2[j][1]):
      i +=1 
    elif p1[i][0] > p2[j][0] or (p1[i][0] == p2[j][0] and p1[i][1] > p2[j][1]):
      j += 1
    else:
       assert p1[i][0] == p2[j][0] and p1[i][1] == p2[j][1], ("{}.{}".format(p1[i], p2[j]))
       if (p1[i][0] != 0 or p1[i][1] != 0) and abs(p1[i][0]) + abs(p1[i][1]) < min:
         min = abs(p1[i][0]) + abs(p1[i][1])
       i += 1
       j += 1
  return min

print(inters(positions1, positions2))
  

fin = open("input_day2.txt", "r")

for line in fin:
  arr = line.split(",")
arr = [int(x) for x in arr]

arr[1] = 12
arr[2] = 2

pos = 0
while pos+3 < len(arr) and arr[pos] != 99:
  if arr[pos] == 1:
    arr[arr[pos+3]] = arr[arr[pos+1]] + arr[arr[pos+2]]
  elif arr[pos] == 2:
    arr[arr[pos+3]] = arr[arr[pos+1]] * arr[arr[pos+2]]
  else:
   break
  pos +=4
print(arr[0])

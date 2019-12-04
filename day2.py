fin = open("input_day2.txt", "r")

for line in fin:
  arr = line.split(",")
orig_arr = [int(x) for x in arr]

def compute(n,v):
	arr = list(orig_arr)
	arr[1] = n
	arr[2] = v
	pos = 0
	while pos+3 < len(arr) and arr[pos] != 99:
	  if arr[pos] == 1:
	    arr[arr[pos+3]] = arr[arr[pos+1]] + arr[arr[pos+2]]
	  elif arr[pos] == 2:
	    arr[arr[pos+3]] = arr[arr[pos+1]] * arr[arr[pos+2]]
	  else:
	   break
	  pos +=4
	return arr[0]

for n in range(100):
  for v in range(100):
    
    res = compute(n,v)
    print(res)    
    if res == 19690720:
      print("Value ", 100 * n + v) 
      exit(0)

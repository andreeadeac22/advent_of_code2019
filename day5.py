fin = open("input_day5.txt", "r")

for line in fin:
  arr = line.split(",")
orig_arr = [int(x) for x in arr]

def op(arr, pos):
  instr = arr[pos] 
  op = instr % 100
  t1 = (instr % 1000 - op) / 100
  t2 = (instr % 10000 - t1 * 100 - op) / 1000

  if t1 == 0:
      par1 = arr[arr[pos+1]]
  else:
      par1 = arr[pos+1]
  if t2 == 0:
      par2 = arr[arr[pos+2]]
  else:
      par2 = arr[pos+2]

  if op == 1:
    return par1 + par2
  if op == 2:
    return par1 * par2
  raise Exception("op should have been 1 or 2, but it's ", op)

def compute():
  arr = list(orig_arr)
  pos = 0
  while pos < len(arr) and arr[pos] != 99:
    if arr[pos] % 100 == 3:
      # ask for input
      pos+=1 
      par = int(input())
      arr[arr[pos]] = par
    elif arr[pos] % 100 == 4:
      # output
      pos +=1
      if arr[pos] // 100 == 1:
          print(arr[pos])
      else:
          print(arr[arr[pos]])
    else:
        print("Opcode ", arr[pos])
        arr[arr[pos+3]] = op(arr, pos)
        pos +=3
    pos += 1
  return arr[0]

compute()


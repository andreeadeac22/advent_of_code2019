fin = open("input_day5.txt", "r")

for line in fin:
  arr = line.split(",")
orig_arr = [int(x) for x in arr]

def oper(arr, pos):
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

  return op, par1, par2

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
        #print("Opcode ", arr[pos])
        op, par1, par2  = oper(arr, pos)
        if op == 1:
            arr[arr[pos+3]] = par1 + par2
            pos += 3
        if op == 2:
            arr[arr[pos+3]] = par1 * par2
            pos +=3
        if op == 5:
            if par1 != 0:
                pos = par2 - 1
            else:
                pos += 2
        if op == 6:
            if par1 == 0:
                pos = par2 - 1
            else:
                pos += 2
        if op == 7:
            arr[arr[pos+3]] = int(par1 < par2)
            pos += 3
        if op == 8:
            arr[arr[pos+3]] = int(par1 == par2)
            pos += 3
    pos += 1
  return arr[0]

compute()


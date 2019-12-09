fin = open("input_day6.txt", 'r')
lines = fin.read().splitlines()

notzd = set() # set of ids which don't have zero in_degree
id_node_dict = {} #XYZ - id
neigh_node = {} # id_from : id_to


num_node = 0 
for line in lines:
    nodes = line.split(')')
    print(nodes)
    n1 = nodes[0]
    n2 = nodes[1]
    if n1 not in id_node_dict:
        id_node_dict[n1] = num_node
        num_node +=1
    if n2 not in id_node_dict:
        id_node_dict[n2] = num_node
        num_node +=1
    idn1 = id_node_dict[n1]
    idn2 = id_node_dict[n2]
    
    neigh_node[idn2] = idn1 
    notzd.add(idn1)

print(notzd)
print(id_node_dict)
print(neigh_node)

orbits = num_node * [0]  # o[node_id] = num_orbits 

def dfs(root, orbits):
    if orbits[root] != 0:
        return orbits[root] 
    
    if root in neigh_node:
      res = 1 + dfs(neigh_node[root], orbits)
    else:
      res = 0
    orbits[root] = res
    return res


for i in range(num_node):
    if i not in notzd:
        # end node
        _ = dfs(i, orbits)
        #print(sum(orbits))

print(sum(orbits))

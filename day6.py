fin = open("input_day6.txt", 'r')
lines = fin.read().splitlines()

notzd = set() # set of ids which don't have zero in_degree
id_node_dict = {} #XYZ - id
neigh_node = {} # id_from : id_to
node_id_dict = {} # id - XYZ

num_node = 0 
for line in lines:
    nodes = line.split(')')
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
    
    node_id_dict[idn1] = n1
    node_id_dict[idn2] = n2
    
    if idn2 not in neigh_node:
      neigh_node[idn2] = [idn1]
    else:
      neigh_node[idn2].append(idn1)
    # for part 2
    if idn1 not in neigh_node:
       neigh_node[idn1] = [idn2]
    else:
      neigh_node[idn1].append(idn2)   
    notzd.add(idn1)

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

"""
for i in range(num_node):
    if i not in notzd:
        # end node
        _ = dfs(i, orbits)
        #print(sum(orbits))

print(sum(orbits))
"""

dist = num_node * [0]
def bfs(root, dist):
  dist[root] = 1
  visited = []
  visited.append(root)
  curr_pos = 0
  last = 0
  while curr_pos <= last:
    if visited[curr_pos] in neigh_node:
      for neigh in neigh_node[visited[curr_pos]]:
        if neigh == id_node_dict['SAN']:
          return dist[visited[curr_pos]] + 1
        if dist[neigh] == 0:
          dist[neigh] = dist[visited[curr_pos]] + 1
          last += 1
          visited.append(neigh)
    curr_pos +=1
  return dist[id_node_dict['SAN']]

print(bfs(id_node_dict['YOU'], dist))

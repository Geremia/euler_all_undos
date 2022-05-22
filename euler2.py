def eulerCycle(G, start): # G = graph (dictionary)
  path = [start]
  #construct a set of all edges in graph:
  edgesRemaining = set()
  for n in G.keys():
    for neighbor in G[n]:  # neighbor is a neighbor of node.
      edgesRemaining.add((n,neighbor))
  print("edgesRemaining:", edgesRemaining)
  n = start
  for neighbor in G[n]:
    edge = (n,neighbor)
    if edge in edgesRemaining:
      edgesRemaining.remove(edge)
      path.append(neighbor)
    if neighbor == start and len(edgesRemaining)!=0:
      return path
    else:
      n = neighbor
  return path

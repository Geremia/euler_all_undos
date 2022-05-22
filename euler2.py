#!/usr/bin/python3

def eulerCycle(G, start): # G = graph (dictionary)
  path = [start]
  #construct a set of all edges in graph:
  edgesRemaining = set()
  for n in G.keys():
    for neighbor in G[n]:  # neighbor is a neighbor of node.
      edgesRemaining.add((n,neighbor))
  n = start
  while True:
    neighbor = G[n]

    edge = (n,neighbor)
    if edge in edgesRemaining:
      edgesRemaining.remove(edge)
      path.append(n)
    if len(edgesRemaining)==0:
      return path
    n = neighbor
  return 0

eulerCycle({0:[1],1:[0,2],2:[1,0]}, 1)

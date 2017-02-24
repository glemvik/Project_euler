# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:55:05 2017

@author: Gunvor


The following undirected network consists of seven verticess and twelve edges with a total weight of 243.

The same network can be represented by the matrix below.
    	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-

However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty verticess, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

Solution is found in less than 1 second.

@author: gunvor
"""

from collections import defaultdict
from time import time

def get_edges(filename):
    """
    Returns number of vertices in the network, weight of the heaviest edge and
    list (indexed by vertices) of defaultdictionaries of neighbour vertices and 
    corresponding weight of edge between them.
    """
    vertice = 0
    maximum_edge = 0
    edges = []
    
    file = open(filename)
    for line in file:
        edges.append(defaultdict(int))
        neighbours = line.strip().split(',')
        
        # ADD EDGE BETWEEN CURRENT VERTICES IF IT EXISTS
        for i in range(0,len(neighbours)):
            if neighbours[i] != '-':
                edges[vertice][i] = int(neighbours[i])
                maximum_edge = max(maximum_edge, int(neighbours[i]))
        vertice += 1
    file.close()
    
    return vertice, maximum_edge, edges

# READ EDGES FROM FILE INTO DEFAULTDICTIONARY AND FIND MAXIMUM EDGE AND 
# NUMBER OF VERTICES IN NETWORK FOR LATER USE
start_time = time()
vertices, maximum_edge, edges = get_edges('107_network.txt')

# COMPUTE WEIGHT OF ALL EDGES
total_weight = sum([sum(edges[i].values()) for i in range(0,vertices)])//2                  
print('Number of vertices:', vertices)

# PREPARE FOR PRIM'S ALGORITHM
tree = set()
tree.add(0)
weight = 0

# RUN PRIM'S ALGORITHM
while len(tree) < vertices:
    minimum_edge = maximum_edge + 1

    for i in tree:
        for key,value in edges[i].items():
            if value < minimum_edge and key not in tree:
                minimum_edge = value
                new_vertices = key
        
    tree.add(new_vertices)
    weight += minimum_edge

# RESULTS
print('Weight of minimum spanning tree:',weight)
print('Maximum saving:', total_weight - weight)
print('Time:', time() - start_time)
# -*- coding: utf-8 -*- 
# Problem URL: https://projecteuler.net/problem=79
""" 
 
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
 
"""
from time import time
from collections import defaultdict
from operator import itemgetter

DEBUG = False
PROGRESS = False

def dprint(*args):
    if DEBUG:
        print(*args)
        
def pprint(*args):
    if PROGRESS:
        print(*args)


def DFS(vertices, edges, source):
    """
    Depth first search of a directed acyclic graph (DAG), provided a source node. 
    Returns the post-orderings of the DAG. 
    """
    # PREPARE FOR DFS
    unvisited = set(vertices)
    pre = defaultdict(None)
    post = defaultdict(None)
    
    # INITIALIZE
    clock = 1
    to_explore = [source]

    # BEGIN DFS
    while clock <= 2*len(vertices):
        
        dprint('Stack: {}'.format(to_explore))
        
        # PEEK AT STACK
        vertex = to_explore[-1]

        dprint('Exploring {}'.format(vertex))

        # ASSIGN PRE-NUMBER AND MARK AS VISITED
        if vertex in unvisited:
            pre[vertex] = clock
            dprint('   pre[{}] = {}'.format(vertex,clock))
            clock += 1
            unvisited.remove(vertex)
        
        # GET NEIGHBOURS
        neighbours = edges[vertex]
        dprint('   neighbours: {}'.format(neighbours))
        
        for neighbour in neighbours:
            
            # ADD FIRST UNVISITED NEIGHBOUR TO STACK
            if neighbour in unvisited:
                dprint('   {} is unvisited'.format(neighbour))
                to_explore.append(neighbour)
                break
        
        # PEEK AT STACK TO DETERMINE WHETHER OR NOT TO GIVE POST-NUMBER
        new_vertex = to_explore[-1]
        
        if new_vertex == vertex:
            post[vertex] = clock
            dprint('   post[{}] = {}'.format(vertex,clock))
            clock += 1
            to_explore.pop()

    return post


#------------------------------------------------------------------------------
#---------------------------------- M A I N -----------------------------------
#------------------------------------------------------------------------------

start_time = time()


vertices = set()
edges = defaultdict(set)

# READ VERTICES AND EDGES FROM FILE
with open('p079_keylog.txt') as file:
    for line in file:
        digits = []
        for vertex in line.strip():
            digits.append(int(vertex))
            vertices.add(int(vertex))
               
        for i in range(len(digits)-1):
            edges[digits[i]].add(digits[i+1])

# FOUND SOURCE FROM PREVIOUS ATTEMPT AT SOLVING PROBLEM
source = 7

# GET POST-NUMBERING OF VERTICES IN DFS, TO LINEARIZE THE DAG
post = DFS(vertices, edges, source)

# FIND LINEARIZATION
linearization = ''
for key,value in sorted(post.items(), key = itemgetter(1)):
    linearization = str(key) + linearization

print(linearization)
print('Time:', time() - start_time)
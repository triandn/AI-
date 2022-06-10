import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import heapq

V = ["S", "A", "B", "C", "D", "E", "F", "G", "H"]
E = [("S", "A"), ("S", "B"), ("S", "C"), ("A", "D"), ("A", "B"),
     ("B", "D"), ("B", "F"), ("B", "G"), ("C", "F"),
     ("D", "E"), ("F", "E"), ("E", "G"), ("F", "H"), ("H", "G")]


graph = {}
for node in V:
    temp_list = []
    for edge in E:
        if edge[0] == node:
            temp_list.append(edge[1])
    graph[node] = temp_list
print(graph)
    
def DFS(inputState, goalState):
    frontier = [inputState]
    explorer = []
    while frontier:
        state = frontier.pop((len(frontier)-1))
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in graph[state]:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False

def BFS(inputState, goalState):
    frontier = [inputState]
    explorer = [] 
    while frontier:
        state = frontier.pop(0)
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in graph[state]:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False


print("Result of DFS: ")
result = DFS('S', 'H')
if result:
    s = 'explored '
    for i in result:
        s  += i + ' '
        print(s)
else: 
    print('Khong tim thay duong di')
    
print("\n")
print("Result of BFS: ")
result = BFS("S" , "H")
if result:
    s = 'explored '
    for i in result:
        s  += i + ' '
        print(s)
else: 
    print('Khong tim thay duong di')

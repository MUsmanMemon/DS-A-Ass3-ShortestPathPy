# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:22:18 2021

@author: Muhammad Usman Memon
"""

import math;

# Ask User to input file name into the console.
filename = input("Please enter the name of the file along with extension: ")
# filename = 'a3-debug.txt'
print("The filename you entered is "+ filename)
maxsize = 10000

class Vertex:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

# Python program to read file
with open(filename,'r', encoding="utf8") as file:
    firstline = next(file).split()
    firstline = [int(x) for x in firstline]
    
    #Initializing the Matrix to a 0 matrix for Vertices x Vertices. The we loop through the edges to fill the matrix
    adjMatrix = []
    for i in range(firstline[0]):
        adjMatrix.append([0 for k in range(firstline[0])])
    
    vertices = [None for k in range(firstline[0])]
    # a = [None for k in range(firstline[0])]
    #Storing the vertices data in an array according to vertex index for Euclidian Distance
    for j in range(firstline[0]):
        # vertices.append(next(file).split())
        test = next(file).split()
        # a.append(test[1:])
        vertices[int(test[0])-1] = test[1:]
        # x = Vertex(int(test[0]), int(test[1]), int(test[2]))
        # a[j] = x
        vertices[int(test[0])-1] = [int(x) for x in vertices[j]]
      
        #Building the vertices and edges Adjacency Matrix to store graph data
    # edges = list()
    for i in range(firstline[1]):
        test = next(file).split()
        test = [int(x) for x in test]
        adjMatrix[test[0]-1][test[1]-1] = test[2]
        if adjMatrix[test[1]-1][test[0]-1] == 0:
            adjMatrix[test[1]-1][test[0]-1] = test[2]
        # edges.append(test)
        
    test = next(file).split()
    start = int(test[0])
    end = int(test[1])
    # end = 10
#     # print(start) testing
#     # print(end)
    
def euclidian(start,end):
    diff1 = start[0]-end[0]
    diff2 = start[1]-end[1]
    result = math.sqrt((diff1**2)+(diff2**2))
    
    return result


steps = []; secSteps = []
#Class to solve the graph
class Graph:

    #Find the minimum dist value from vetices in queue
    def minDistance(self,dist,queue):
        minimum = maxsize
        min_index = -1
        
        #Pick the vertex from the dist array which has least distance and is still in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index


    #Saving the shortest path to our destination
    def savePath(self, parent, j, path):
        
        if parent[j] == -1 :
            
            path.append(j+1)
            return
        self.savePath(parent , parent[j],path)
       
        path.append(j+1)


    def dijkstra(self, graph, src, path):
        # path = []
        rows = len(graph)
        cols = len(graph[0])

        #This store the distance of all vertices from the src, since we are doing minimum dist we use max value initialized
        dist = [maxsize] * rows


        #Array to store the path tree, store the previous parent
        # global parent 
        parent = [-1] * rows

        # Distance of source vertex from itself is always 0
        dist[src] = 0
    
        # Add all vertices in queue
        queue = []
        for i in range(rows):
            queue.append(i)
            
        #Find shortest path for all vertices
        while queue:

            #From the vertices still in queue pick the vertice with the minimum distance
            u = self.minDistance(dist,queue)

            # pop out the minimum value element   
            queue.remove(u)

            #From the U vertex we scan through its neighbours and update dist[] values and parent index for vertices in the quuee
            for i in range(cols):
                #check if there is an edge between i and u and if there is data in dist[i]
                if graph[u][i] and i in queue:
                    #Then check if dist[i] from src is less than the dist[u] + the edge between u and i
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u 

        self.savePath(parent, end-1, path)
        # edges.append(dist[end-1])
        return dist[end-1]

    #get 2nd shortest by removing each edge in shortest and compare  
    def secondShortestPath(self, graph, src, path) : 
        #store previous vertex's data  	
        abc = []
        mylist = steps[:] 
        global gandu
        gandu = [[] for e in range(len(mylist)-1)]  #Store the different paths for different short distances without edge
        prevy = -1 #initialize privy to store previous edge info
        preS = -1 #hold previous vertex info
        preD = -1 #hold previous vertex info

        for i in range(len(mylist)-1) :
            #get source and destination for each path in shortest path
            s = mylist[i]-1
            d = mylist[i + 1]-1
            #resume the previous path 
            if (prevy != -1) :
                graph[preS][preD] = prevy
                graph[preD][preS] = prevy       
            #record the previous data for recovery
            prevy = graph[s][d]
            preS = s
            preD = d
            #remove this path
            graph[s][d] = 0
            graph[d][s] = 0
            #calculate shortest distance and path
            abc.append(self.dijkstra(graph, src, gandu[i]))
        return abc

obj = Graph()


# Print the solution
shortestDistance = obj.dijkstra(adjMatrix,start-1, steps)
# path1 = g.savePath(pt, end-1)
#Outputs expected
#Number of edges and number of vertices in the Graph
print("The number of Vertices in the Graph is "+str(firstline[0])+" and edges is "+str(firstline[1]))
print("Finding the shortest path between vertices "+str(start)+" and "+str(end))
#Printing the Euclidian Distance
print("\nThe Euclidian Distance is :" , end="  ")
print(euclidian(vertices[start-1], vertices[end-1]))
#The shortest path to the end Vertice
print("The shortest Path is :" , end="  ")
for x in steps: print(x, end=" ")

print("\nShortest Path length is ", shortestDistance)

# print("\n Now for the second shortest")
lxyz = obj.secondShortestPath(adjMatrix, start-1, secSteps)

shorty = float('inf')
indy = None
for h,i in enumerate(lxyz):
    if i< shorty:
        shorty= i
        indy = h
        
# print(shorty)
# print(indy)
print("The second Shortest distance for the Start and End vertices is: ")
print("Distance : "+ str(shorty))
print("Path : ", end="  ")
for g in gandu[indy]: print(g, end=" ")


#Python program to print topological sorting of a DAG
from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List o(1)
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v) #o(1)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]: #O(v)
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack) #O(E)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self): #O(V^2+ E)
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V): #O(V)
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Print contents of stack
        print(stack)

    def another_top_path(self, order):
        self.
        counter = 0
        for i in range(len(order)):
            if i == self.graph[i]:
                pass
            else:
                counter += 1
        if counter != 0:
            print("There is another path")
        else:
            print("This is the same path")


g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
#g.addEdge(1, 5);
order = [5,4,2,3,1,0]
g.another_top_path(order)

#print("Following is a Topological Sort of the given graph")
#g.topologicalSort()

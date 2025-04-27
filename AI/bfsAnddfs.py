graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=[]  #track the node you visited as no node visited twice
queue=[]     #first in first out 
def bfs(visited,graph,node):
    visited.append(node)  #starting node is visited 
    queue.append(node)    #Staring node in the queue
    while queue:
        m=queue.pop(0)   # remove the front from the queue
        print(m,end=" ")
        for neighbour in graph[m]: 
            if neighbour not in visited: 
                visited.append(neighbour)
                queue.append(neighbour)
print("The BFS is:\n")
bfs(visited,graph,'5')

# Time Complexity O(V+E)
#Space complexity O(V)

graph2={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited2=[]

def dfs(visited2,graph2,node):
    if node not in visited2: # check if the node visted
        print(node, end=" ") #if not then print
        visited2.append(node) # and maked as visited
        for neighbour in graph2[node]: # check the neighbour node 
            dfs(visited2,graph2,neighbour) # recursively call the dfs function for each neighbour
print("\nDFS is:")
dfs(visited2,graph2,'5')


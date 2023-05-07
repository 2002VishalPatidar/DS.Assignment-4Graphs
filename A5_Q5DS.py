
adj=[]

def addEdge (u, v):
    adj[u].append(v)

def checkCycleUtil (node, visited, inStack):

    if (inStack[node] == True):
        return True
    
    
    if (visited[node] == True):
        return False
    
    
    visited[node] = True

    
    inStack[node] = True

    
    for v in adj[node]:
        if (checkCycleUtil(v, visited, inStack) == True):
            return True
    

  
    inStack[node] = False

    return False


def checkCycle(V, E):
    
    visited = [False] * V
    inStack = [False] * V
    
    
    for i in range(V):
        if (checkCycleUtil(i, visited, inStack) == True):
            return True
        

    return False


V, E = 5, 7


adj = [[] for i in range(V)]

addEdge(0, 1)
addEdge(0, 4)
addEdge(0, 2)
addEdge(1, 3)
addEdge(2, 3)
addEdge(4, 1)
addEdge(4, 2)

if(checkCycle(V, E)):
    print("YES")
else:
    print("NO")


from typing import List




class Graph:
    
    def addEdge(adj,u,v,isDirected):
        adj[u].append(v)
        if not isDirected:
            adj[v].append(u)
    size = 3
    adj = [list()*i for i in range(size)]
    
                    
   
    
    def dfsUtil(self,source,destination,count):
        if source == destination:
            return count
        else:
            for u in self.adj[source]:
                count+=1
                self.dfsUtil(u,destination=destination,count=count)
        return count
   
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        W = len(edges)
        
        a = [1]
        
        
        for i in range(n):
            self.addEdge(self.adj,edges[i][0],edges[i][1],True)
        count = self.dfsUtil(source,destination,count)
        return count == 0
        
        


if __name__ == "__main__":
    n = 3; edges = [[0,1],[1,2],[2,0]]; source = 0; destination = 2
    g = Graph()
    print(g.validPath(n,edges,source,destination))    
    

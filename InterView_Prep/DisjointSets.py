from typing import List
from unittest import main


class UnionFind:
    
    """
    Union-Find: Three variants-> Quick Union, Quick Find, Union Find By Rank(optimised version)
    All applications of disjoint sets
    """
    
    def init(self, size) -> None:
        self.root = [0]*size
        self.rank = [i for i in range(size)]
        
    
    def find(self,x):
        if self.root[x]==x:
            return x
        else:
            self.root[self.root[x]]=self.find(self.root[x])
        return x
    
        
        
    
    def union(self,x,y):
        
        rootX=self.find(x)
        rootY = self.find(y)
        
        
        if self.rank[rootX] < self.rank[rootY]:
                self.root[rootY]=rootX
        elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX]=rootY
        else:
                self.root[rootX]=rootY
                self.rank[rootY]+=1
                     
    
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.init(n)
        W = len(edges)
        for i in range(len(edges)):
            self.union(edges[i][0],edges[i][1])
        print(self.root)
        print(self.rank)
        print(self.root[source])
        print(self.root[destination])
        print(self.connected(source,destination))
        return self.connected(self.root[source],self.root[destination])
    
   
            
            

if __name__ == "__main__":
    n = 3; edges = [[0,1],[1,2],[2,0]]; source = 0; destination = 2
    n1 = 6; edges1 = [[0,1],[0,2],[3,5],[5,4],[4,3]]; source1 = 0; destination1 = 5
    uf = UnionFind()
    n2=10
    edges2=[[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]]
    source2=1
    d2=0
    
    print(uf.validPath(n,edges=edges,source=source,destination=destination))
    print(uf.validPath(n1,edges1,source1,destination1))
    print(uf.validPath(n2,edges2,source2,d2))
    
            
        
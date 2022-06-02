from functools import lru_cache
from typing import List
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return results
    
    """
        For DP Solution
        nextNode∈neighbors(currNode),allPathsToTarget(currNode)={currNode+allPathsToTarget(nextNode)}
    """  
    def allPathsSourceTargetV2(self, graph: List[List[int]]) -> List[List[int]]:
    
        target = len(graph) - 1

        # apply the memoization
        @lru_cache(maxsize=None)
        def allPathsToTarget(currNode):
            if currNode == target:
                return [[target]]

            results = []
            for nextNode in graph[currNode]:
                for path in allPathsToTarget(nextNode):
                    results.append([currNode] + path)

            return results

        return allPathsToTarget(0)  
    
if __name__ == "__main__":
    graph = [[1,2],[3],[3],[]]
    allpaths = Solution()
    print(allpaths.allPathsSourceTarget(graph=graph)) 
    print(allpaths.allPathsSourceTargetV2(graph)) 
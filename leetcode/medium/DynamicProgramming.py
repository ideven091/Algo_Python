import math
from unittest import main


class EditDistance:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1)]*(m+1)
        print(dp) 
        for i in range(n+1):
            #print(dp)
            for j in range(m+1):
                if i == 0:
                    dp[i][j]=j
                elif j == 0:
                    dp[i][j]=i
                    print(dp)
                elif word1[i-1]==word2[j-1]:
                    print(word1[i-1])
                    dp[i][j]=dp[i-1][j-1]

                else:
                    dp[i][j]=1+min(dp[i-1][j],(min(dp[i][j-1],dp[i-1][j-1])))
        print(dp)
        return dp[m][n]

    def minDistanceV2(self,word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0]*(m+1)]*(n+1)
        for i in range(n+1):
            dp[i][0]=-1
        
    def f(self,i,j,word1,word2,dp):
        pass

            
class DynamicProgrammingProblems:
    distance = EditDistance()
    word1 = "horse"
    word2 = "horse"
    print(distance.minDistance(word1=word1,word2=word2))

DynamicProgrammingProblems()



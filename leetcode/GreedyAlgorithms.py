

from typing import List


class Activity:
    def __init__(self):
        self.start = 0
        self.end = 0

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        i = 0
        res = 0
        while res<=amount:

            if coins[i]<=amount:
                amount -= coins[i]
                res += 1
            else:
                i += 1

        return res


if __name__ == "__main__":
    a = Solution()
    coins = [10,5,9,1]
    print(a.coinChange(coins,20))




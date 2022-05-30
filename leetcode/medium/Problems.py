from typing import List

class Solution:
    """_summary_
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        
        
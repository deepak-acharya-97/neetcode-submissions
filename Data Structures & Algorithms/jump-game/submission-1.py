"""
https://neetcode.io/problems/jump-game
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True
        # if nums[0] == 0:
        #     return False

        dp = {}

        def util(index):
            if index == n - 1:
                return True
            if index >= n:
                return True
            if nums[index] == 0:
                return False
            if index in dp:
                return dp[index]
            for j in range(nums[index]):
                result = util(index+j+1)
                if result:
                    dp[index] = True
                    return True
            dp[index] = False
            return False

        def greedy_approach():
            goal = n - 1
            for index in range(n-2, -1, -1):
                if index + nums[index] >= goal:
                    goal = index
            return goal == 0

        # return util(0)
        return greedy_approach()

# nums=[1,2,1,0,1]
# print(Solution().canJump(nums))

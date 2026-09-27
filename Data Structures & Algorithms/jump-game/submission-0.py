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

        def util(index):
            if index == n - 1:
                return True
            if index >= n:
                return True
            if nums[index] == 0:
                return False
            for j in range(nums[index]):
                result = util(index+j+1)
                if result:
                    return True
            return False

        return util(0)

# nums=[1,2,1,0,1]
# print(Solution().canJump(nums))

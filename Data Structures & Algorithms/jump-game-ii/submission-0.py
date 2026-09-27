from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = {}

        def util(index):
            if index == n - 1:
                return 0
            if index >= n:
                return 0
            if nums[index] == 0:
                return float("inf")
            if index in dp:
                return dp[index]
            result = float("inf")
            for j in range(nums[index]):
                result = min(result, 1 + util(index+j+1))
            dp[index] = result
            return result

        return util(0)

# nums=[2,1,2,1,0]
# print(Solution().jump(nums))
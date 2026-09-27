from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(index, current_subset):
            if index >= n:
                result.append(current_subset)
                return

            #consider the element at ith index
            dfs(index+1, current_subset + [nums[index]])
            #do not consider element at ith index
            dfs(index+1, current_subset)

        dfs(0, [])
        return result

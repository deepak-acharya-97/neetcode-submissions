from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(index, current_subset):
            if index >= n:
                result.append(current_subset.copy())
                return

            #consider the element at ith index
            current_subset.append(nums[index])
            dfs(index+1, current_subset)
            current_subset.pop()
            dfs(index+1, current_subset)
            
        dfs(0, [])
        return result

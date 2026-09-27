from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        def util(index, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            if index >= n or total > target:
                return

            util(index, subset + [nums[index]], total + nums[index])
            util(index + 1, subset, total)

        util(0, [], 0)
        return result

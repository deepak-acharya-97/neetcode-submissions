"""
https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def approach_1_binary_search():
            l, r = 0, len(nums) - 1
            result = float("inf")

            while l <= r:
                if nums[l] < nums[r]:
                    result = min(result, nums[l])
                    break
                m = l + (r - l) // 2
                result = min(result, nums[m])
                if nums[l] <= nums[m]: #left part sorted, min exists in right
                    l = m + 1
                else:
                    r = m - 1

            return result

        def lower_bound():
            l, r = 0, len(nums) - 1

            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return nums[l]

        # return approach_1_binary_search()
        return lower_bound()


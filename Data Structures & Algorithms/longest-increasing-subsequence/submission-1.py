from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        def n2():
            lis = 1
            for i in range(1, n):
                for j in range(0, i):
                    if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        lis = max(lis, dp[i])
            print(dp)
            return lis

        def get_position(value, arr):
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] > value:
                    high = mid
                else:
                    low = mid + 1
            return low

        def upper_bound(target, arr):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def lower_bound(target, arr):
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def nlogn():
            lis = 0
            dp = []

            for num in nums:
                if not dp or num > dp[-1]:
                    dp.append(num)
                    lis += 1
                    continue

                index = lower_bound(num, dp)
                print(index)
                dp[index] = num

            return lis


        # return n2()
        return nlogn()

nums=[9,1,4,2,3,3,7]
print(Solution().lengthOfLIS(nums))
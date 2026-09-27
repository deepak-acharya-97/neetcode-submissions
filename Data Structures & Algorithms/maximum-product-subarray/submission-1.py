class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def max_product(nums):
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            max_product = float('-inf')
            for i in range(1, n):
                dp[i] = max(dp[i-1]*nums[i], nums[i])
                max_product = max(max_product, dp[i])
            return max_product

        def max_product_bottom_up(nums):
            result = nums[0]
            curr_min = 1
            curr_max = 1
            for elem in nums:
                temp = curr_max * elem
                curr_max = max(curr_max * elem, curr_min * elem, elem)
                curr_min = min(temp, curr_min * elem, elem)
                result = max(result, curr_max)
            return result
        return max_product_bottom_up(nums)

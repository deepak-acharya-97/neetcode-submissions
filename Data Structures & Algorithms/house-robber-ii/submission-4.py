class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        def dfs(i, end_index, dp):
            if i > end_index:
                return 0
            if (end_index - i) == 1:
                return max(nums[i], nums[end_index])
            if i in dp:
                return dp[i]
            rob = nums[i] + dfs(i+2, end_index, dp)
            do_not_rob = dfs(i+1, end_index, dp)
            dp[i] = max(rob, do_not_rob)
            return dp[i]

        # def dfs(i, start_index, end_index, dp):
        #     print("i >> ", i)
        #     if i > end_index:
        #         print("BASE CASE 1, i out of bound - returning i >> ", i)
        #         return 0
        #     if i < start_index:
        #         print("BASE CASE 2, i out of bound - returning i >> ", i)
        #         return 0
        #     if (end_index - i) == 1:
        #         print("BASE CASE 3, ONLY 2 Elements - returning max >> ", i, end_index)
        #         return max(nums[i], nums[end_index])
        #     if i in dp:
        #         return dp[i]
        #     rob = nums[i] + dfs(i+2, start_index, end_index, dp)
        #     do_not_rob = dfs(i+1, start_index, end_index, dp)
        #     dp[i] = max(rob, do_not_rob)
        #     print("ANSWER i, end_index >> result", i, end_index, dp[i])
        #     return dp[i]
        # dp = {}
        return max(dfs(0, n-2, {}), dfs(1, n-1, {}))
        # return dfs(1, 1, n-1, dp)

            

        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total%2 == 1:
            return False
        target = total / 2
        def dfs(i, curr_sum, dp):
            if i >= n:
                return False
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            
            consider = dfs(i+1, curr_sum + nums[i], dp)
            do_not_consider = dfs(i+1, curr_sum, dp)
            dp[(i, curr_sum)] = consider or do_not_consider
            return dp[(i, curr_sum)]
        dp = {}
        return dfs(0, 0, dp)
        
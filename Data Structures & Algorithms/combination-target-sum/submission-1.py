class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(i, subset, c_sum):
            if i >= n:
                return
            if c_sum > target:
                return 
            if c_sum == target:
                result.append(subset)
                return
            dfs(i, subset+[nums[i]], c_sum+nums[i])
            dfs(i+1, subset, c_sum)

        dfs(0, [], 0)
        return result
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def dfs(i, curr):
            if i >= n:
                result.append(curr)
                return
            dfs(i+1, curr + [nums[i]])
            dfs(i+1, curr)

        dfs(0, [])
        return result
        
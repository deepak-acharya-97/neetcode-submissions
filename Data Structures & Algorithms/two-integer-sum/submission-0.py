class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}

        for i in range(len(nums)):
            a = target - nums[i]
            if a in sol:
                return [sol[a], i]
            sol[nums[i]] = i
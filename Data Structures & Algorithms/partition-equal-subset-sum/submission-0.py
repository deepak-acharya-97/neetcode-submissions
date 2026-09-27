from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        def util(index, curr_target):
            if curr_target == 0:
                return True

            if index <= 0:
                return False

            if nums[index-1] > curr_target:
                return util(index-1, curr_target)

            consider = util(index-1, curr_target-nums[index-1])
            do_not_consider = util(index - 1, curr_target)
            
            return consider or do_not_consider
        
        return util(len(nums), target)

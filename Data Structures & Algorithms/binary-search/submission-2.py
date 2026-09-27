from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def standard():
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1

        def upper_bound():
            l, r = 0, len(nums)

            while l < r:
                print(f"{l=}, {r=}")
                mid = l + (r - l)//2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
                print(f"[Updated] {l=}, {r=}")

            return l - 1 if l > 0 and nums[l - 1] == target else -1

        def lower_bound():
            l, r = 0, len(nums)

            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            return l if l < len(nums) and nums[l] == target else -1

        # return standard()
        # return upper_bound()
        return lower_bound()
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = set()

        def util(index, subset, total):
            if total == target:
                result.add(tuple(sorted(subset.copy())))
                return
            if index >= n or total > target:
                return

            util(index + 1, subset + [candidates[index]], total + candidates[index])
            util(index + 1, subset, total)

        util(0, [], 0)
        return list([list(_) for _ in result])
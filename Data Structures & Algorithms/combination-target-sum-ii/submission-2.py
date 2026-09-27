from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def brute_force():
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

        def approach_2():
            n = len(candidates)
            candidates.sort()
            result = []

            def util(index, subset, total):
                if total == target:
                    result.append(subset.copy())
                    return
                if index >= n or total > target:
                    return

                util(index + 1, subset + [candidates[index]], total + candidates[index])
                while index + 1 < n and candidates[index] == candidates[index + 1]:
                    index += 1
                util(index + 1, subset, total)

            util(0, [], 0)
            return result

        return approach_2()

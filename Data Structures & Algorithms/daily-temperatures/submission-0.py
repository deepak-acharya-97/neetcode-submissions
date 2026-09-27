from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for ind, val in enumerate(temperatures):
            if not stack:
                stack.append((val, ind))
            else:
                while stack and stack[-1][0] < val:
                    (curr_val, curr_ind) = stack.pop()
                    result[curr_ind] = ind - curr_ind
                stack.append((val, ind))
        return result

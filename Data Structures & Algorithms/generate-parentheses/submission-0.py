from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        def util(open_count, close_count, expression):
            if (n-close_count) > (n-open_count):
                return 0
            if open_count < 0 or close_count < 0:
                return 0
            if open_count == 0 and close_count == 0:
                combination.append(expression)
                return 1
            add_open_paranthesis = util(open_count-1, close_count, expression+'(')
            add_close_paranthesis = util(open_count, close_count-1, expression+')')
            return add_close_paranthesis + add_open_paranthesis
        result = util(n, n, "")
        return combination

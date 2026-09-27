class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_map = {')': '(', '}': '{', ']': '['}
        open_paranthesis = {'(', '{', '['}
        stack = []
        for ch in s:
            if ch in open_paranthesis:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != paranthesis_map[ch]:
                    return False
                stack.pop()
        if len(stack) > 0:
            return False

        return True

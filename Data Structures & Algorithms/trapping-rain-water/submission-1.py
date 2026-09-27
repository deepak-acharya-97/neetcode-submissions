class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            print(f"{l=}, {r=}, {leftMax=}, {rightMax=}")
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                print(f"Updated Left Max to {leftMax} (Current Height = {height[l]}), Previous Result = {res}")
                res += leftMax - height[l]
                print(f"Updated Result = {res}")
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                print(f"Updated Right Max to {rightMax} (Current Height = {height[r]}, Previous Result = {res})")
                res += rightMax - height[r]
                print(f"Updated Result = {res}")
        return res
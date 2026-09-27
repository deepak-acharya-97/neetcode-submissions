class Solution:
    def climbStairs(self, n: int) -> int:
        def util(stair_position):
            if stair_position < 0:
                return 0
            if stair_position == 0:
                return 1

            return util(stair_position-1) + util(stair_position-2)

        return util(n)

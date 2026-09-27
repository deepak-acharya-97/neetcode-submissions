class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        result = 0
        local_min_index = 0
        for index, value in enumerate(prices):
            local_min = prices[local_min_index]
            if value < local_min:
                local_min_index = index
            else:
                result = max(result, value - local_min)
        return result
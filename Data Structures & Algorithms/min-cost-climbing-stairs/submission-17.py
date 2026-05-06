class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, next = 0, 0
        for i in range(2, n + 1):
            next1 = min(next + cost[i - 1], prev + cost[i - 2])
            prev = next
            next = next1
        return next
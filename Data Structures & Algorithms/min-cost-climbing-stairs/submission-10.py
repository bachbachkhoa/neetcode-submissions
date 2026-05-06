class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = 0
        p2 = 0

        for i in range(2, len(cost) + 1):
            p3 = min(cost[i - 2] + p1, cost[i - 1] + p2)
            p1 = p2
            p2 = p3
        return p3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        prev, next = 1, 2
        for i in range(3, n + 1):
            next1 = prev + next
            prev = next
            next = next1
        return next
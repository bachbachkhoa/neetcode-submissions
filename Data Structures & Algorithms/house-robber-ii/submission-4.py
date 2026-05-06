class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) in [1, 2]:
            return max(nums)
        p1 = nums[0]
        p2 = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            p3 = max(p2, p1 + nums[i])
            p1, p2 = p2, p3
        r1 = p2
        p1 = nums[1]
        p2 = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            p3 = max(p2, p1 + nums[i])
            p1, p2 = p2, p3
        r2 = p2
        return max(r1, r2)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) in [1, 2]:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(dp)):
            dp[i] = max([dp[x] + nums[i] for x in range(i - 1)])
        return max(dp)
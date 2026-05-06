class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpMax = [0] * n
        dpMin = [0] * n
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        for i in range(1, n):
            dpMax[i] = max(nums[i], nums[i] * dpMax[i - 1], nums[i] * dpMin[i - 1])
            dpMin[i] = min(nums[i], nums[i] * dpMax[i - 1], nums[i] * dpMin[i - 1])
        return max(dpMax)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = sum(range(0,max(nums)+1)) - sum(nums)
        if result == 0:
            return max(nums) + 1 if min(nums) == 0 else 0
        else:
            return result

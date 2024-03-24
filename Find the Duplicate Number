class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                return nums[i]
                break
            i += 1

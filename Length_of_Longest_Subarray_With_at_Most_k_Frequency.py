from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left = 0
        max_length = 0
        
        for right, num in enumerate(nums):
            freq[num] += 1
            
            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

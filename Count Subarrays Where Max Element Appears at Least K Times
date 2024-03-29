from collections import Counter
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
    
        def countMaxSubarrays(nums, k, max_num):
            count = 0
            window_start = 0
            max_count = 0
            
            for window_end in range(len(nums)):
                if nums[window_end] == max_num:
                    max_count += 1
                    
                while max_count >= k:
                    count += len(nums) - window_end
                    if nums[window_start] == max_num:
                        max_count -= 1
                    window_start += 1
                        
            return count
        
        max_num = max(nums)
        result += countMaxSubarrays(nums, k, max_num)
                    
        return result

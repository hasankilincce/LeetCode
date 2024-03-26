from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = set(x for x in nums if x > 0)  # Just take positives
        if not positives:  # If there any positive, return 1
            return 1
        i = 1
        while i in positives:
            i += 1
        return i

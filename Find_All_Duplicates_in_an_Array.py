from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [x for x, num in Counter(nums).items() if num == 2]

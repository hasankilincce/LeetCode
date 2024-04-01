class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = list(s.split(" "))
        words = [i for i in word if len(i) > 0]
        print(words)
        return len(words[-1])

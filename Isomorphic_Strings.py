from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def find_repeat(x):
            result = []
            count = 1
            for i in range(len(x) - 1):
                if x[i] == x[i+1]:
                    count += 1
                else:
                    result.append(count)
                    count = 1
            result.append(count)
            return result

        if (find_repeat(s) == find_repeat(t)) and (list(Counter(s).values()) == list(Counter(t).values())):
            return True
        else:
            return False

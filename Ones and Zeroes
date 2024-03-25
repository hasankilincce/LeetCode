from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        elements = []
        numZero = 0
        numOne = 0
        results = []

        for i in strs:
            i = list(i)
            i.append("0")
            i.append("1")
            i.sort()
            x,y = Counter(i).values()
            x -= 1
            y -= 1
            elements.append([x,y,(x+y)])

        k = 0
        while k <= 5:
            if k == 0:
                sortedElements = sorted(elements, key=lambda x:(x[0], x[1], x[2]))
            elif k == 1:
                sortedElements = sorted(elements, key=lambda x:(x[0], x[2], x[1]))
            elif k == 2:
                sortedElements = sorted(elements, key=lambda x:(x[1], x[2], x[0]))
            elif k == 3:
                sortedElements = sorted(elements, key=lambda x:(x[1], x[0], x[2]))
            elif k == 4:
                sortedElements = sorted(elements, key=lambda x:(x[2], x[1], x[0]))
            elif k == 5:
                sortedElements = sorted(elements, key=lambda x:(x[2], x[0], x[1]))

            numZero = 0
            numOne = 0
            result = 0
            for j in sortedElements:
                if ((j[0] + numZero) <= m) and ((j[1] + numOne) <= n):
                    result +=1
                    numZero += j[0]
                    numOne += j[1]
            print(result)
            results.append(result)
            k+=1
        return max(results)

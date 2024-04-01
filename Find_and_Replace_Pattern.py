class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        demoList=[]
        for i in pattern:
            demoList.append(pattern.count(i))
        result=[]
        for i in (words):
            step=[i.count(j) for j in i]    
            if step==demoList and [*map(i.index,i)]==[*map(pattern.index,pattern)]:
                result.append(i)
        return result

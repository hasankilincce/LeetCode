# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        testList = []
        while head is not None:
            testList.append(head.val)
            head = head.next
        i = 0
        while i < int(len(testList)/2)+1:
            if testList[i] == testList[-i-1]:
                i+=1
            else:
                break

        if i >= len(testList)/2:
            return True
        else:
            return False

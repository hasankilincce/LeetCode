# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        test = []
        n = head
        while n is not None:
            test.append(n.val)
            n = n.next
        test.reverse()
        if test:
            head = ListNode(test[0])
            tail = head
            i=1
            while i < len(test):
                tail.next = ListNode(test[i])
                tail = tail.next
                i += 1
            return head
        else:
            return None

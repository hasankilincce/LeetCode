class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head1 = list1

        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        
        prev_a = None
        next_b = list1
        for _ in range(a):
            prev_a = next_b
            next_b = next_b.next
        for _ in range(b - a + 1):
            next_b = next_b.next

        if prev_a:
            prev_a.next = list2
        else:
            head1 = list2
        tail2.next = next_b
        
        return head1

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        node_values = []
        current = head
        while current:
            node_values.append(current.val)
            current = current.next
        
        reordered_values = []
        left, right = 0, len(node_values) - 1
        while left <= right:
            reordered_values.append(node_values[left])
            if left != right:
                reordered_values.append(node_values[right])
            left += 1
            right -= 1
        
        current = head
        for val in reordered_values[1:]:
            current.next = ListNode(val)
            current = current.next

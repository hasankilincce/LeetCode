# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        test1 = []
        test2 = []
        n1 = l1
        n2 = l2
        while n1 is not None:
            test1.append(n1.val)
            n1 = n1.next
        while n2 is not None:
            test2.append(n2.val)
            n2 = n2.next

        i, j= 0, 0
        if len(test1) >= len(test2):
            while i < len(test2):
                a = test1[i]
                b = test2[i]

                test2[i] = (a + b)

                i += 1
            while i < len(test1):
                test2.append(test1[i])
                i+=1
            test2.append(0)
            while j < len(test2):
                if test2[j] >= 10:
                    test2[j] = test2[j] % 10
                    test2[j+1] +=1
                j+=1
            if test2[-1] == 0:
                test2.pop()
            resultArray = test2

        else:

            while i < len(test1):
                a = test1[i]

                b = test2[i]

                test1[i] = (a + b)

                i += 1

            while i < len(test2):
                test1.append(test2[i])

                i += 1

            test1.append(0)

            while j < len(test1):

                if test1[j] >= 10:
                    test1[j] = test1[j] % 10

                    test1[j + 1] += 1

                j += 1

            if test1[-1] == 0:
                test1.pop()
            resultArray = test1
        e = 1
        head = ListNode(resultArray[0])
        tail = head
        while e < len(resultArray):
            print(head)
            tail.next = ListNode(resultArray[e])
            tail = tail.next
            e+=1
        return head 

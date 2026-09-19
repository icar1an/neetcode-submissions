# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        blanklist = []
        while head:
            blanklist.append(head.val)
            head = head.next
        dummy = ListNode()
        tail = dummy
        for i in range(len(blanklist)-1, -1, -1):
            n = ListNode()
            tail.next = n
            n.val = blanklist[i]
            tail = tail.next
        return dummy.next

        

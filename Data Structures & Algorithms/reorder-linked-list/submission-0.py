# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        l2 = slow.next
        slow.next = None
        l1 = head

        prev = None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt

        l2 = prev

        while l2:                   
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2
            




                
        
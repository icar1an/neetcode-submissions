"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head
        curr2 = head
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        nodes[None] = None
        while curr2:
            nodes[curr2].next = nodes[curr2.next]
            nodes[curr2].random = nodes[curr2.random]
            curr2 = curr2.next
        return nodes[head]




            
        
                
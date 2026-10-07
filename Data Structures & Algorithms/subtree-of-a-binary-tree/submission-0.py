# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def sameTree(p, q):
    pqueue = [p]
    qqueue = [q]

    while pqueue and qqueue:
        pnode = pqueue.pop()
        qnode = qqueue.pop()
        if not pnode and not qnode:
            continue
        elif not pnode or not qnode:
            return False
        elif pnode.val != qnode.val:
            return False
        else:
            pqueue.append(pnode.left)
            pqueue.append(pnode.right)
            qqueue.append(qnode.left)
            qqueue.append(qnode.right)
    return True
        
            
        


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        toTraverse = [root]
        while toTraverse:
            node = toTraverse.pop()
            if node is None:
                continue
            if sameTree(node, subRoot):
                return True
            toTraverse.append(node.left)
            toTraverse.append(node.right)
        return False

        
        
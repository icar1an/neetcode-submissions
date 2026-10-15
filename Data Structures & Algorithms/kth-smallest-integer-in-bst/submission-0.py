# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root):
    toTraverse = [root]
    allnodes = [root.val]
    while toTraverse:
        node = toTraverse.pop()
        if node.left is not None:
            toTraverse.append(node.left)
            allnodes.append(node.left.val)
        if node.right is not None:
            toTraverse.append(node.right)
            allnodes.append(node.right.val)
    return allnodes

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        allnodes = dfs(root)
        allnodes = sorted(allnodes)
        return allnodes[k-1]

        
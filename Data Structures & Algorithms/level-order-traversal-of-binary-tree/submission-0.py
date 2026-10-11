# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrderRec(root, level, res):
    # Base case
    if root is None:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.val)

    # Recur for left and right children
    levelOrderRec(root.left, level + 1, res)
    levelOrderRec(root.right, level + 1, res)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        levelOrderRec(root, 0, res)
        return res

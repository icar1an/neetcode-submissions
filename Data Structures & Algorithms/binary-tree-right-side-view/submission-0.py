# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrderRec(root, level, res):
    if root is None:
        return
    
    if len(res) <= level:
        res.append([])

    res[level].append(root.val)

    levelOrderRec(root.left, level+1, res)
    levelOrderRec(root.right, level+1, res)
    
    

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        levelOrderRec(root, 0, res)
        output = []
        for level in res:
            output.append(level[-1])
        return output
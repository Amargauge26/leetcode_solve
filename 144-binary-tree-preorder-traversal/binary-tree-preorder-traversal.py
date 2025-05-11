# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pre(node,res):
            if not node:
                return []
            res.append(node.val)
            pre(node.left,res)
            pre(node.right,res)
        res=[]
        pre(root,res)
        return res
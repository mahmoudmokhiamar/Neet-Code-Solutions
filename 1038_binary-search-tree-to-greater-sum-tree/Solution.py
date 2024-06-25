# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.current_sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if not root:
                return 
            else:
            
                traverse(root.right)
                self.current_sum += root.val
                root.val = self.current_sum    
                traverse(root.left)
        traverse(root)
        return root 
                
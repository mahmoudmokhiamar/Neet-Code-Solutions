# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.LCA = TreeNode(float('inf'))
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current = root 
        #execute inf until finding the desired node
        while current: 
            #if p and q are less than current go look for LCA in left subtree since there are lower nodes
            if p.val < current.val and q.val < current.val:
                current = current.left
            #if p and q are greater than current go look for LCA in right subtree since there are lower nodes
            elif p.val > current.val and q.val > current.val:
                current = current.right
            #else we either are at p or q or at a split were value is between p and q (edge cases)
            else:
                return current
       
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return 
        #draw it for better interpretability

        
        #preorder first node is always the root
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid]) #next root which is left to the current is going to be to the right of mid in index (we need both arrays for none)
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:]) #everything after the mid is to the right of the root.
        return root
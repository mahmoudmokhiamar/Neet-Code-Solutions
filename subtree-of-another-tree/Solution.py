# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(s,t):
            ##both are null they are the same
            if not s and not t:
                return True
            ##check trees from equal roots
            elif s and t and s.val == t.val:
                ##recursively check other parts
                return helper(s.right,t.right) and helper(s.left,t.left)
                ##check if they are the same left and right
            ##third condition is one of them is null, hence can't be the same
            return False
        
        #if first tree is nonempty and second tree is empty then it's a subTree
        if not subRoot:
            return True
        #if root is empty then other cannot be a subtree
        elif not root and subRoot:
            return False
        #recursevilty check same trees
        elif helper(root,subRoot):
            return True

        
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        

        


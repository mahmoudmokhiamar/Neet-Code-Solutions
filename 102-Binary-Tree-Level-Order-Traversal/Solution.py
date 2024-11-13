# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     # self.list = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level_length = len(queue)
            level_nodes = []

            for i in range(level_length):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level_nodes.append(node.val)
            if level_nodes:
                res.append(level_nodes)
        return res
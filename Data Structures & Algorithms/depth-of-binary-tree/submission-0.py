# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, leng):

            if node is None:
                return (leng-1)
            
            leng1 = dfs(node.left, leng+1)
            leng2 = dfs(node.right, leng+1)

            return max(leng1, leng2)
            
        
        return dfs(root, 1)
        

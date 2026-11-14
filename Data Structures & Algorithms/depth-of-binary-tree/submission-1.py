# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(node, leng):
            if node is None:
                return leng-1
            
            
            leng1 = rec(node.left, leng+1)
            leng2 = rec(node.right, leng+1)
            ans = max(leng1, leng2)
            
            return ans

        return rec(root, 1)
       

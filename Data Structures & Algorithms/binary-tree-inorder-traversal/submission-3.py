class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        ans = []
        def rec(node):

            if node is None:
                return node

            rec(node.left)
            ans.append(node.val)
            rec(node.right)
            
        rec(root)
        return ans

    
    
        

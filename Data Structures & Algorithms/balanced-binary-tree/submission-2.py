# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            if leftHeight is False or rightHeight is False:
                ans = False
                return False
            else:
                diff = leftHeight - rightHeight  
                print('diff is',diff)
                if abs(diff) > 1:
                    ans = False
                    return False
            print(leftHeight, rightHeight)
            
            return max(leftHeight, rightHeight) + 1

        dfs(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
              
        self.sum = 0
        
        def leafSum(root, s):
            
            if not root:
                return
            
            if not root.left and not root.right:
                self.sum += s * 10 + root.val
                
            leafSum(root.left, s*10 + root.val)
            leafSum(root.right, s*10 + root.val)
        
        s = 0
        leafSum(root, 0)
        return self.sum

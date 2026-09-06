# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        left = root.left
        right = root.right

        if left and not left.val < root.val:
            return False
        elif right and not right.val > root.val:
            return False
        
        return self.isValidBST(left) and self.isValidBST(right)
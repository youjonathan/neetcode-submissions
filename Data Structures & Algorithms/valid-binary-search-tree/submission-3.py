# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        maxi = math.inf
        mini = -math.inf

        def isValidSub(root, maxi, mini):
            if not root:
                return True
            
            if root.val > maxi or root.val < mini:
                return False

            left = root.left
            right = root.right

            if left and not left.val < root.val:
                return False
            elif right and not right.val > root.val:
                return False
            
            return isValidSub(left, root.val, mini) and isValidSub(right, maxi, root.val)
        
        return isValidSub(root, maxi, mini)
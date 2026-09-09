# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # we want to recurse down
        global_max = -math.inf

        def findMaxSum(root: Optional[TreeNode]) -> int:
            nonlocal global_max
            if not root:
                return 0

            left_sum = max(0, findMaxSum(root.left))
            right_sum = max(0, findMaxSum(root.right))
            global_max = max(global_max, root.val + left_sum + right_sum)
            return root.val + max(left_sum, right_sum)

        maxSum = findMaxSum(root)
        global_max = max(global_max, maxSum)
        return global_max
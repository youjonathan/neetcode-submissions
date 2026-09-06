# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # this seems simple with an array
        arr = []

        def storeValues(root):
            if not root:
                return
            storeValues(root.left)
            arr.append(root.val)
            storeValues(root.right)
        
        storeValues(root)

        return arr[k - 1]
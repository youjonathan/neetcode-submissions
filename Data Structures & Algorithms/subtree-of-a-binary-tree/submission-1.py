# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # my first guess is going down each node to check for the same
        # value as the subroot, and then when you hit that, go down
        # a function that checks if the subroot is correct
        # this seems brute force, but I can't think of a better solution

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                    return True
            return False

        if not root:
            return False

        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
                
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
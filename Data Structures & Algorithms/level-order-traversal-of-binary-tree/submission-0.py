# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        nest = list()
        
        def addToNest(root: Optional[TreeNode], level: int):
            if not root:
                return
            if len(nest) == level:
                nest.append([])
            nest[level].append(root.val)
            addToNest(root.left, level + 1)
            addToNest(root.right, level + 1)

        addToNest(root, 0)

        return nest
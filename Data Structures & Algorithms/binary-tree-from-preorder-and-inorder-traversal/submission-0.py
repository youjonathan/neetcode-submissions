# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        # preorder always has the root first
        # inorder than allows us to split by the root
        root = preorder[0]
        split_i = inorder.index(root)

        i_left = inorder[:split_i]
        i_right = inorder[split_i + 1:]

        p_left = preorder[1 : len(i_left) + 1]
        p_right = preorder[len(i_left) + 1:]

        node = TreeNode(val=root)
        node.left = self.buildTree(p_left, i_left)
        node.right = self.buildTree(p_right, i_right)

        return node
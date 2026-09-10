# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # val,left.val,n,left.right.val,n,n, etc
        serial = ""

        # 1,2,n,n,3,4,n,n,5,n,n
        def addNode(root: Optional[TreeNode]):
            nonlocal serial
            if not root:
                serial += "n,"
                return
            serial = serial + str(root.val) + ","
            addNode(root.left)
            addNode(root.right)

        addNode(root)
        return serial
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(',')
        i = 0

        def build():
            nonlocal i
            this = tokens[i]
            i += 1
            if this == 'n':
                return None
            else:
                node = TreeNode(int(this))
                node.left = build()
                node.right = build()
                return node
            # your existing logic: 'n' → None; else make node, build left, build right, return node

        root = build()
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val, None, None)
            return root

        if val > root.val:
            print(root.val)
            if not root.right:
                root.right = TreeNode(val, None, None)
                return root
            elif val == root.val + 1 and val == root.right.val - 1:
                tmpright = root.right
                root.right = TreeNode(val, None, tmpright)
                return root
            else:
                self.insertIntoBST(root.right, val)
                return root
        elif val < root.val:
            print(root.val)
            if not root.left:
                root.left = TreeNode(val, None, None)
                return root
            elif val == root.val - 1 and val == root.left.val + 1:
                tmpleft = root.left
                root.left = TreeNode(val, tmpleft, None)
                return root
            else:
                self.insertIntoBST(root.left, val)
                return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if key == root.val:
            '''if not root.left and not root.right:
                return None'''
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                leftsubtree = root.left
                rightsubtree = root.right
                new = leftsubtree
                while new.right:
                    new = new.right
                new.right = rightsubtree
                return leftsubtree

            

        elif key > root.val:
            if not root.right:
                return root
            else:
                root.right = self.deleteNode(root.right, key)
                return root
        elif key < root.val:
            if not root.left:
                return root
            else:
                root.left = self.deleteNode(root.left, key)
                return root

        
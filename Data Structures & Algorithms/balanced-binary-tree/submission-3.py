# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lh, lbal = self.height(root.left)
        rh, rbal = self.height(root.right)
        if lbal == False or rbal == False:
            return False
        if abs(lh - rh) > 1:
            return False
        else:
            return True


    def height(self, root):
        # h = 0; lh = 0; rh = 0
        if not root:
            return (0, True)

        lh, lbal = self.height(root.left)
        rh, rbal = self.height(root.right)

            
        h = 1 + max(rh,lh)
        if lbal == False or rbal == False:
            return (h, False)
        elif abs(lh - rh) > 1:
            return (h, False)
        else:
            return (h, True)




    def inorder(self, root):
        output = []
        if not root:
            return []
        output += self.inorder(root.left)
        output += root.val
        output += self.inorder(root.right)

        return output
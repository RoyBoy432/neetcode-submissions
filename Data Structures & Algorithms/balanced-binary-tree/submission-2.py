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
        
        lh2 = self.height(root.left)
        rh2 = self.height(root.right)
        if lh2[1] == False or rh2[1] == False:
            return False
        if abs(lh2[0] - rh2[0]) > 1:
            return False
        else:
            return True


    def height(self, root):
        # h = 0; lh = 0; rh = 0
        if not root:
            return tuple([0, True])

        lh = self.height(root.left)
        rh = self.height(root.right)

            
        h = 1 + max(rh[0],lh[0])
        if lh[1] == False or rh[1] == False:
            return tuple([h, False])
        elif abs(lh[0] - rh[0]) > 1:
            return tuple([h, False])
        else:
            return tuple([h, True])




    def inorder(self, root):
        output = []
        if not root:
            return []
        output += self.inorder(root.left)
        output += root.val
        output += self.inorder(root.right)

        return output
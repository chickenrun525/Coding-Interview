# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root.val
        elif p.val > root.val and q.val < root.val:
            return root.val
        elif q.val > root.val and p.val < root.val:
            return root.val
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        

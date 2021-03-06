# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        answer = []
        if not root:
            return answer
        curr_level = [root]
        while curr_level:
            level_result = []
            next_level = []
            for each in curr_level:
                level_result.append(each.val)
                if each.left:
                    next_level.append(each.left)
                if each.right:
                    next_level.append(each.right)
            answer.append(level_result)
            curr_level = next_level
        return answer
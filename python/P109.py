# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        return self.sortedArrayToBST(nums)
        
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[length/2])
        root.left = self.sortedArrayToBST(nums[:length/2])
        root.right = self.sortedArrayToBST(nums[length/2+1:])
        return root
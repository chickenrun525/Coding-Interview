class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        answer = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in answer:
                    answer.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                 i += 1
        return answer
                
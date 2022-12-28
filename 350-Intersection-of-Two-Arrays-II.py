"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Solution 1"""
        # nums = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             nums.append(nums1[i])
        #             nums2[j] = -1
        #             break
        # return nums

        """Solution 2"""
        # nums1 = sorted(nums1)
        # nums2 = sorted(nums2)
        # check = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             check.append(nums1[i])
        #             nums2[j] = -1
        #             break
        # return check

        """Solution 3"""
        counter = {}
        num = []
        for i in range(len(nums1)):
            if counter.get(nums1[i]) == None:
                counter[nums1[i]] = 1
            else:
                counter[nums1[i]] += 1

        for item in nums2:
            if item in counter and counter.get(item) > 0:
                counter[item] -= 1
                num.append(item)
        return num

    """Solution 4"""
    i = 0
    j = 0
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    nums = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            nums.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
    return nums

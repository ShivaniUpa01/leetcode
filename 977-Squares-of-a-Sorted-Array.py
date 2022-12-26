"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""
# Solution 1
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums

# Solution 2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        mini = float(inf)
        mid = 0
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        for i in range(len(nums)):
            if mini > nums[i]:
                mini = nums[i]
                mid = i
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        i = len(nums1)-1
        j = 0
        while i >= 0 and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i -= 1
            else:
                result.append(nums2[j])
                j +=1
        while i >= 0 or j < len(nums2):
            if i >= 0 :
                result.append(nums1[i])
                i -= 1
            if j < len(nums2):
                result.append(nums2[j])
                j += 1
        return result
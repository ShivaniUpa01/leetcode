"""Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """Solution 1"""
        k = k % len(nums)
        n = len(nums)
        mid = n - k
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        result = []
        for i in range(len(nums2)):
            result.append(nums2[i])
        for i in range(len(nums1)):
            result.append(nums1[i])
        for i in range(len(result)):
            nums[i] = result[i]
        """Solution 2"""
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
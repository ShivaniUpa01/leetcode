"""53. Maximum Subarray
Given an integer array nums, find the subarray which has the largest sum and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = 0
        j = i+1
        add = nums[i]
        maxn = float(-inf)
        while j < len(nums):
            if add > maxn:
                maxn = add
            if add <= 0:
                i += 1
                j = i + 1
                add = nums[i]
            else:
                add = add + nums[j]
                j += 1
        if add > maxn:
            maxn = add
        return maxn
        """https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/?envType=study-plan&id=data-structure-i&orderBy=most_votes"""
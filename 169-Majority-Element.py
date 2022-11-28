"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
"""

""" Solution 1 """
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = 0
        nmax = float(-inf)
        ndict = {}
        for i in range(len(nums)):
            if ndict.get(nums[i]) == None:
                ndict[nums[i]] = 1
            else:
                ndict[nums[i]] = ndict[nums[i]] + 1
        # print(ndict)
        for k, v in ndict.items():
            if v > nmax:
                n = k
                nmax = v

        return n
    """Solution 2:- Brute Force"""

    class Solution:
        def majorityElement(self, nums):
            majority_count = len(nums) // 2
            for num in nums:
                count = sum(1 for elem in nums if elem == num)
                if count > majority_count:
                    return num

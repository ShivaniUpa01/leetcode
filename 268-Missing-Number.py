"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""

"""Solution 1"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        allnums = {}
        for i in range(len(nums)+1):
            allnums[i] = 0
        for i in range(len(nums)):
            if allnums.get(nums[i]) == 0:
                allnums[nums[i]] = 1
        for k, v in allnums.items():
            if v == 0:
                return k


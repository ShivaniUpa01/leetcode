"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
"""

"""language specification Solution"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#         twice = {}
#         for i in range(len(nums)):
#             if twice.get(nums[i]) == None:
#                 twice[nums[i]] = 1
#             else:
#                 return True
#         return False

"""Solution """
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        twice = {}
            for i in range(len(nums)):
                if twice.get(nums[i]) == None:
                    twice[nums[i]] = 1
                else:
                    return True
            return False
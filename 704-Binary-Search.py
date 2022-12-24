"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
 to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
# Solution 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        mid = 0
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1
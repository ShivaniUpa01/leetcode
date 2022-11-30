"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique,
or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation:The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences."""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = {}
        count = []
        for i in range(len(arr)):
            if unique.get(arr[i]) == None:
                unique[arr[i]] = 1
            else:
                unique[arr[i]] = unique[arr[i]] + 1
        print(unique)
        for i in sorted(unique.values()):
            count.append(str(i))
        print(count)
        for i in range(len(count)-1):
            if count[i] == count[i+1]:
                return False
        return True
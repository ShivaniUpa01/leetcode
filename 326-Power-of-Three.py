"""Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33
"""

"""Solution 1"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (1162261467 % n == 0)
"""Solution 2"""
        # if n == 0 or n == -1:
        #     return False
        # while n != 1:
        #     if n % 3 == 0:
        #         n = n // 3
        #     else:
        #         return False
        # return True
"""Solution 3"""
        # i = 0
        # result = 0
        # while result < n:
        #     result = 3 ** i
        #     if result == n:
        #         return True
        #     i += 1
        # return False
"""Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        n = str(abs(x))
        check = ""
        for i in range(len(n) - 1, -1, -1):
            check += n[i]
        if int(check) == x:
            return True
        return False
"""Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding
column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:

Input: columnTitle = "A"
Output: 1
"""
"""Solution 1"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = columnTitle[::-1]
        n = 0
        rem = 0
        result = 0
        for i in range(len(columnTitle)):
            n = ord(col[i])
            rem = n - 64
            result += (26 ** i) * rem
        return result



"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist,
 return -1.
Example 1:
Input: s = "leetcode"
Output: 0
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = {}
        for i in range(len(s)):
            if check.get(s[i]) != None: #and check.get(s[i]) == i:
                check[s[i]] = -1
            elif check.get(s[i]) == None:
                check[s[i]] = i
        for i in range(len(s)):
            if check.get(s[i]) != -1:
                return i
        return -1
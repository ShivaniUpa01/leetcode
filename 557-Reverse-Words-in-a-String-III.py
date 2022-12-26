"""557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and
initial word order.
Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""
# Solution 1
class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split()
        i = 0
        for item in s:
            s[i] = item[::-1]
            i +=1
        return  " ".join(s)
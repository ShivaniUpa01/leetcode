"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""
"""Solution 1"""
def dictonary(s,dictS):
    for i in range(len(s)):
        if dictS.get(s[i]) == None:
            dictS[s[i]] = 1
        else:
            dictS[s[i]] = dictS[s[i]] + 1
    return dictS


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) != len(t):
            return False
        dictS = dictonary(s , dictS)
        for item in t:
            if dictS.get(item) == None:
                return False
            else:
                dictS[item] = dictS[item] -1
                if dictS[item] < 0:
                    return False
        for k, v in dictS.items():
            if v != 0:
                return False
        return True
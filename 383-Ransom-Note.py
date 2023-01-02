"""383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
"""
# Solution 1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = 0
        while n <= len(magazine):
            print(magazine[i:n])
            if ransomNote == magazine[i:n]:
                return True
            else:
                i += 1
                n += 1
        return False
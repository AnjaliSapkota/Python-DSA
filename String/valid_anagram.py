# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# using hash map: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char,0) + 1
        for char in t:
            if char not in count:
                return False
            elif count[char] == 0:
                return False
            else:
                count[char] -= 1
        return True

    
# by sorting: O(nlogn)

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         return sorted(s) == sorted(t)


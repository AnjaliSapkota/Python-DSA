# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        result = []
        p_count = {}
        window_count = {}

        for char in p:
            p_count[char] = p_count.get(char,0) + 1
        
        for i in range (len(p)):
            char = s[i]
            window_count[char] = window_count.get(char,0) + 1
        
        if window_count == p_count:
            result.append(0)

        # slide the window

        left = 0

        for right in range(len(p), len(s)):
            char = s[right]
            window_count[char] = window_count.get(char,0) + 1

            char = s[left]
            window_count[char] -=1

            if window_count[char] == 0:
                del window_count[char]
                
            left += 1

            if window_count == p_count:
                result.append(left)
        return result
# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
 
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:

                # Delete left character OR right character
                return (isPalindrome(left + 1, right) or
                        isPalindrome(left, right - 1))

            left += 1
            right -= 1

        return True
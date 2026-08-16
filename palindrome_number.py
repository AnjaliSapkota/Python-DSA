# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        reversed = 0
        while temp > 0:
            rem = temp % 10
            reversed = reversed * 10 + rem
            temp = temp / 10

        return x == reversed

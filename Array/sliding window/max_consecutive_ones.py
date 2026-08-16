# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = 0
        maxcount = 0
        j = 0
        n = len(nums)

        while j < n:
            if nums[j] == 1:
                current_count += 1
                j += 1
            else:
                maxcount = max(maxcount, current_count)
                current_count = 0
                j += 1

        return max(maxcount, current_count)
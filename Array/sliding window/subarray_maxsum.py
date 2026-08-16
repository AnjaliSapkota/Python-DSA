#  Maximum Sum of  Subarrays With Length K

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        windowsum = 0

        for i in range(k):
            windowsum += nums[i]

        maxsum = windowsum

        for j in range(k,n):
            windowsum += nums[j]
            windowsum -= nums[j-k]

            maxsum = max(maxsum, windowsum)

        return maxsum
        
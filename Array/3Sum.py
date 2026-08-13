# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Brute force method (uncomment to run)

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         result = []
#         for i in range(n-2):
#             for j in range(i+1,n-1):
#                 for k in range(j+1,n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         triplet = [nums[i], nums[j], nums[k]]
#                         triplet = sorted([nums[i], nums[j], nums[k]])
#                         if triplet not in result:
#                             result.append(triplet)

#         return result


# Two Pointer Method:

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0

        output = []

        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                result = nums[i] + nums[j] + nums[k]

                if result == 0:
                    triplet = [nums[i], nums[j], nums[k]]

                    if triplet not in output:
                        output.append(triplet)

                    j += 1
                    k -= 1

                elif result > 0:
                    k -= 1

                else:
                    j += 1

            i += 1

        return output
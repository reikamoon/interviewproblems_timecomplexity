# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Restate: Find the sum of two numbers that will add up to the targeted number.
#
# Assumptions: There are two numbers that add up to the targeted number.
# Thoughts: I need to scan though the list and find two numbers that will add up to the targeted number.

# Good Inputs: 8 and 7 make 56
# Bad Inputs: Negative number plus a positive number (-2 + 2 does not equal 4!)
#Edge Cases: Negative number and bigger positive number (42 + -2 = 40)
#
# Variable: Value
# sum = targeted number

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
# Time Complexity: O(n) because it has to scan through the whole list to find nums that add up to the target sum
# Space Complexity: O(n)

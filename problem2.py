# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Restate: Find the number that does not repeat in the array
#Assumptions: All numbers repeat except for one, I need to find that one.
#
#Good Inputs: Integers like 1, 2, 3, 4
#Bad Inputs: Non integers
#Edge Cases: Numbers that do appear more than once
#
#Variable: Value
#target = number that does NOT appear more than once

#Thoughts: I can make a separate list. If a new number appears in the array, I add it to the list, if it appears again, I remove it.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

#Time Complexity: O(n)2. We iterate through the numbers taking O(n) time. We search
#through the whole list to find if there is a duplicate number.
#Space Complexity: O(n). We need a list of size n to contain elements in nums.





#

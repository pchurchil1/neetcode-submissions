# nums = array of integers
# Output: The longest count of consecutive integers in nums
# Idea: Sort the numbers then iterate through: O(n log n)
# Idea: Set/Dict the numbers, check if next number is in set/dict: O(n)
#

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if num-1 not in numbers:
                length = 1
                while (num + length) in numbers:
                    length +=1
                longest = max(longest, length)
        return longest


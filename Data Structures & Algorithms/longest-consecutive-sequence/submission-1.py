# nums = array of integers
# Output: The longest count of consecutive integers in nums

# Turn the list into a set O(n), access the set using 'in' O(1), 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for number in nums:
            if number - 1 in nums:
                continue
            else:
                curr = number
                count = 0
                while curr in nums:
                    count +=1
                    curr +=1
                longest = max(longest, count)
        
        return longest




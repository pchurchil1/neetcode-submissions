# Input: List of numbers
# Input: Target number

# Output: Indecies of the two numbers that sum to the tareget
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_dict = {}

        for i, n in enumerate(nums):
            if (target - n) in numbers_dict:
                return [numbers_dict[target-n], i]

            numbers_dict[n] = i
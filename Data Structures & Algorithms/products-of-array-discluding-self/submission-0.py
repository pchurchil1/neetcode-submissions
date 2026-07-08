class Solution:
    # Input: integer array ex. nums = [1,2,4,6]
    # Output: Product of all elements of nums except nums[i] ex. [48,24,12,8]
    #
    # Idea: Brute force it Problem: O(n^2)
    # Idea: Find the product of the whole array then iterate through dividing O(n) Problem: 0s
    # Edge case: 2 or more 0s == 0 across the board
    # Edge case: 1 zero == only when that number is excluded does nums[i] have a nonzero
    # Fix: Count zeros

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeros = 0, 0
        output = []
        for num in nums:
            if num != 0:
                if product == 0:
                    product = num
                else:
                    product = product * num
            else:
                zeros +=1
        # Product is now the product of the array without zeros

        for num in nums:
            if zeros > 1:
                output.append(0)
            elif zeros == 1 and num != 0:
                output.append(0)
            elif zeros ==1 and num == 0:
                output.append(product)
            else:
                output.append(int(product/num))

        return output
# Input: Sorted Array arr
# Input: integers k and x
# k: Number of integers to return
# x: Value the integers are looking to be close to
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ret = []
        for num in arr:
            if len(ret) < k:
                ret.append(num)
            else:
                if abs(x - ret[0]) > abs(x-num):
                    ret.pop(0)
                    ret.append(num)
        return ret
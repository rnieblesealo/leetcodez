from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        # first pass: build missing idx table
        d = {}
        for i, n in enumerate(nums):
            d[n] = i

        # second pass: check missing, pick index
        for i, n in enumerate(nums):
            missing = target - n

            if missing in d and d[missing] != i:
                return [i, d[missing]]


print(Solution.twoSum([3, 4, 5, 6], 7))

# linear time: build dictionary of n entries and then scan it
# linear space: there may be up to as many entries in the dict as there are entries in nums

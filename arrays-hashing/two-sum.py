from typing import List


# ORIG: DID NOT WORK
# class Solution:
#     def twoSum(nums: List[int], target: int) -> List[int]:
#         d = dict()
#
#         # make rearrange dict
#         for i, n in enumerate(nums):
#             d[n] = (i, target - n)
#
#         print(d)
#
#         for key, value in d.items():
#
#             if missing in d:
#                 return [key, d[missing]]
#         return None

# o(n) because 2 linear loops (checking existence in dict is constant)
# remember: rearrange equation!
# problem: if we use value as key, a dupe means an entry gets erased
# soln: use index as key; guaranteed unique
#   also doesn't work; we can't easily find the pair to missing
#       soln: make subtraction result the key, index the value

# gave up...
# real soln:

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        print(indices)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]


# why this works despite dupes:
# only the latest dupe value's index will be stored
#   if we hit an earlier dupe, we can get its idx from the loop and the dupe's
#   from the entry in our dict
# if we have something like [5], t=10:
#   the problem's params are violated, no worrying here

print(Solution.twoSum([5, 5], 10))

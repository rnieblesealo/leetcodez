from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # o(n) both
        # go over each
        # add to set if unseen
        # if seen return true
        # if make end return false
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True
        return False

# edge cases:
# 2 of the same char
#   soln:
#       store as dicts instead; compare dicts
#       counter does this for us

from collections import Counter


class Solution:
    def isAnagram(s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)

        return a == b


Solution.isAnagram(s="racecar", t="carrace")

# instantiating counter = o(len(t)) where t is list length
# space = o(k) where k is length of alphabet, hence o(1)
# (counter will never store more than 26 entries)
#   remember that big o = upper bound!

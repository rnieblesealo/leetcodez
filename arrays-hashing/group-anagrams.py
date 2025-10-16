from typing import List
from collections import Counter, defaultdict

"""
Brute force:
For each entry, do the method we did for the easy anagram problem
as we encounter each, add to the list
this is not optimal, o(n^2) time:
    We are looping over the whole thing for each entry
Output will always be a bunch of lists but they can only contain entries
from original wordlist
Thus o(n) space where n = amt. of input words

Neetcode Time Target: o(m * n) (m = n. strings, n = len. of longest str.)
Neetcode Initial Soln.: sort and group using hashmap
"""

# BRUTE FORCE SOLUTION


class Solution:
    def groupAnagrams_BRUTE(strs: List[str]) -> List[List[str]]:
        # loop over strings
        # sort curr
        # if sorted not in dict, add; key = sorted, val(s) = anagram(s)
        # at the end return the values of the dict

        d = {}
        for s in strs:
            ssort = str(sorted(s))
            if ssort not in d:
                d[ssort] = []
            d[ssort].append(s)
        return d.values()

    # we only care about the frequency...
    # so count the ocurrences of each char is an important hint

    # use use the char frequencies as a key to a dict
    # this makes things linear time; we do one pass to build the keys and another to add stuff based on the keys

    def groupAnagrams_RAFA(strs: List[str]) -> List[List[str]]:
        """
        Hashmap:
            key = dict with frequencies
            value = list of strings with matching frequencies
        Approach:
            1 pass to build the hashmap keys
            another pass to count frequencies in each word and put them in the hashmap buckets
            return the hashmap values
        Amends:
            we don't need pass 2; if no entry for this freq exists, add it and continue
            we also need to sort the counter to ensure that freqs are stored in order
            (the key of the hashmap must be an immutable thing)
        """

        # Pass 1
        d = {}
        for s in strs:
            # FIXME: We need to do sorting here, not ideal.
            # At most we'll need to sort 26 items so constant dropped,
            # but still adds overhead
            freqs = tuple(sorted((Counter(s)).items()))
            if freqs not in d:
                d[freqs] = []
            d[freqs].append(s)
        return list(d.values())

    # NeetCode's solution

    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        Notes:
        - defaultdict for default value to be list, neat
        - This approach avoids sorting above in place of iterating over strs
            - This seems to create less overhead, nice!
        """

        res = defaultdict(list)
        # Iterating over m strings (outer loop)...
        # ...Of n length each (inner loop!)
        for s in strs:
            # 26 letters; indices correspond to letters
            count = [0] * 26

            # Compute the key (frequency table)
            for c in s:
                # Figure out index of letter
                # Add 1 to it to denote freq
                count[ord(c) - ord('a')] += 1

            # Add this string to that frequency which corresponds to it
            res[tuple(count)].append(s)

        # Same old here!
        return list(res.values())


print(Solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))

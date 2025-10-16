from typing import List
from collections import Counter


class Solution:

    def topKFrequent_INITIAL(nums: List[int], k: int) -> List[int]:
        """
        Problem:
            Return the k most ocurring in any order
        Approach:
            Simply counter and return the top 3 keys
        """

        # Count & sort keys; will end up with 2-entry tuples
        # where [0] is the entry
        # ...We sorted these by count!
        freqs = sorted(Counter(nums).items(),
                       key=lambda item: item[1], reverse=True)

        # Add the top k to list and return
        res = []
        for i in range(k):
            res.append(freqs[i][0])

        return res

        """
        Notes:
        - Counting: O(n), sorting: O(log n); both O(n log n)
        - Adding to list O(k); we will at most iterate over k items
        - Time: O(n log n), but we want O(n)!

        NeetCode Answer: USE BUCKET SORT
        """

    # Bucket sort version

    def topKFrequent(nums: List[int], k: int) -> List[int]:
        # Count the numbers:
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # ...Why don't we just use a counter?
        count = dict(Counter(nums))

        # Create as many buckets as there are numbers
        freq = [[] for i in range(len(nums) + 1)]

        # Put each number under its count in the list
        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []

        # Iterate in descending order, starting at last
        # We are effectively iterating over individual buckets
        # starting from the one corresponding to the largest num
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        print(freq)


print(Solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))

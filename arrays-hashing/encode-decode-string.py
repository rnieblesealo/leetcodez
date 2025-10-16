from typing import List


class Solution:
    """
    Problem:
        Encoding a list of strings into 1 string and then decoding it
    Approach (I read it because uh... :D)
    - Length delimiter string
    - e.g. Encoding "hey" "jude"
    - "3.hey4.jude"
        - 3, 4 are the lengths, . is the delimiter
    - Simple... Length and delimiter!
    """

    DELIM = " "

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            # Append len to enc
            enc += str(len(s))

            # Append delim
            enc += self.DELIM

            # Append string itself
            enc += s

        return enc

    def decode(self, s: str) -> List[str]:
        strs = []
        count_str = ""

        # Read length n until delimiter
        for i in range(len(s)):
            c = s[i]

            # Read n chars, add to list
            if c.isdigit():
                count_str += c
                # Continue for entire string
            else:
                i += 1

                count = int(count_str)
                strs.append(s[i: i + count])

                # Don't forget to reset these!
                count = count + i
                count_str = ""
        return strs


soln = Solution()

s = soln.encode(["1,23", "45,6", "7,8,9"])
print(s)
print(soln.decode(s))

# FIXME: This is broken due to the digits above; take a look later :/

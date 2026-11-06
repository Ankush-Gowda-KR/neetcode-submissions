class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s            # the length as text, then the string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0                                       # where the next number starts
        while i < len(s):                           # until the end of s
            j = i
            while s[j] != "#":                      # move j forward to the '#'
                j += 1
            length = int(s[i:j])                    # the digits from i up to j
            res.append(s[j + 1 : j + 1 + length])   # the string right after the '#'
            i = j + 1 + length                      # where the next number starts
        return res
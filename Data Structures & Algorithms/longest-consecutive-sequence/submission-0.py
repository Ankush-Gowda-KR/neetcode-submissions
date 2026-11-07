class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for x in num_set:
            if x-1 not in num_set:

                length = 1
                while x+length in num_set:
                    length+=1
                if length > longest:
                    longest = length
        return longest
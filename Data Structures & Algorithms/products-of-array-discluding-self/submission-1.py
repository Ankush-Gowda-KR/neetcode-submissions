class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n                      # a list of n ones; left[0] stays 1
        for i in range(1, n):               # i = 1, 2, 3
            left[i] = left[i-1] * nums[i-1]             # the previous left product × the number just before i

        right = [1] * n                     # right[n - 1] stays 1
        for i in range(n - 2, -1, -1):      # i = 2, 1, 0: counting down
            right[i] = right[i+1] * nums[i+1]            # the next right product × the number just after i

        output = []
        for i in range(n):
            output.append(left[i] * right[i])        # everything left of i × everything right of i
        return output
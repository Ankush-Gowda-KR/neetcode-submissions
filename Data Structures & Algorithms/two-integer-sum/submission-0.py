class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):              # every position
            for j in range(i+1, len(nums)):  # every position AFTER i
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []                              # never reached: the problem promises one answer
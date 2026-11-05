class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                              # number -> how many times
        for n in nums:
            count[n] = count.get(n, 0) + 1
        order = sorted(count, key=count.get, reverse=True)
        return order[:k]
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n           # tallest bar from the start up to i
        maxRight = [0] * n          # tallest bar from i to the end

        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        maxRight[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):          # goes right to left
            maxRight[i] = max(maxRight[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(maxLeft[i], maxRight[i]) - height[i]
        return res
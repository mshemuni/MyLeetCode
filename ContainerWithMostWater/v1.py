import numpy as np


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        ans = 0
        while left != right:
            ans = max(ans, (right - left) * (min(height[left], height[right])))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans

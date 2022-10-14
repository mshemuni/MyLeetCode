class Solution(object):
    def not_repeating(self, s):
        look = s
        for char in s:
            look = look[1:]
            if char in look:
                return False

        return True

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniques = set(s)
        for i in range(len(uniques), 0, -1):
            slide_amount = len(s) - i
            for j in range(slide_amount + 1):
                text = s[j:i + j]
                if self.not_repeating(text):
                    return len(text)


print(Solution().lengthOfLongestSubstring("pwwekw"))

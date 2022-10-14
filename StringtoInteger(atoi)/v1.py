class Solution(object):
    def isnumeric(self, s):
        return s in map(str, range(10))

    def all_isnumeric(self, number):
        all_values = [self.isnumeric(c) for c in number]
        if len(all_values) == 0:
            return False
        return all([self.isnumeric(c) for c in number])

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()
        if len(s) == 0:
            return 0

        sign = ""
        if s.startswith("-"):
            sign = "-"
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        else:
            if not self.all_isnumeric(s[0]):
                return 0

        number = ""
        for char in s:
            if self.all_isnumeric(char):
                number += char
            else:
                break

        if not self.all_isnumeric(number):
            return 0

        the_number = int(sign + number)
        if the_number < -2 ** 31:
            return -2 ** 31
        elif the_number > (2 ** 31 - 1):
            return 2 ** 31 - 1
        else:
            return the_number

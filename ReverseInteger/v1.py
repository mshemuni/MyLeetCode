class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = ""
        if x < 0:
            sign = "-"
            integer = str(x)[1:]
        else:
            integer = str(x)[:]

        rev = int(sign + integer[::-1])

        if rev > (2 ** 31 - 1) or rev < -2 ** 31:
            return 0

        return rev

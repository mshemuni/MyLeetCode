class Solution(object):

    def __isPal(self, values):
        for i in range(int(len(values)/2)):
            if values[i] != values[-i-1]:
                return False

        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        this_value = head
        while this_value.next is not None:
            values.append(this_value.val)
            this_value = this_value.next

        values.append(this_value.val)

        return self.__isPal(values)

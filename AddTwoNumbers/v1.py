class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        v1 = l1
        v2 = l2

        res = ListNode()
        it = 0
        while v1 is not None or v2 is not None:


            if v1 is None:
                value1 = 0
            else:
                value1 = v1.val

            if v2 is None:
                value2 = 0
            else:
                value2 = v2.val

            s = value1 + value2 + carry
            x = res
            for _ in range(it):
                x = x.next

            x.next = ListNode(s % 10)

            it += 1

            carry = s//10

            if v1 is not None:
                v1 = v1.next
            if v2 is not None:
                v2 = v2.next

        if carry != 0:
            x.next.next = ListNode(carry)

        return res.next

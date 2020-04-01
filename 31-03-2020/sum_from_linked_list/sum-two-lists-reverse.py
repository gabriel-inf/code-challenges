# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def convertToInteger(self, list):
        string = ""
        while list:
            string = string + str(list.val)
            list = list.next
        return int(string[len(string)::-1])


    def addTwoNumbers(self, l1, l2, c = 0):

        result = self.convertToInteger(l1) + self.convertToInteger(l2)
        reversed_result = str(result)[len(str(result))::-1]

        root = ListNode(int(str(reversed_result)[0]))
        tail = root
        for n in (range(1, len(str(reversed_result)))):
            tail.next = ListNode(int(str(reversed_result)[n]))
            tail = tail.next
        return root

# first number:
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# second number
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)


while result:
    print (result.val)
    result = result.next

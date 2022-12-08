"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def listToNum(temp):
    i = 0
    num = 0
    while temp != None:
        num = temp.val * 10 ** i + num
        temp = temp.next
        i += 1
    return num


def insertAtEnd(self, new_data):
    new_node = ListNode(new_data)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        num1 = listToNum(temp1)
        num2 = listToNum(temp2)
        add = str(num1 + num2)
        head = ListNode(0)
        curr = head
        for num in reversed(add):
            curr.next = ListNode(num)
            curr = curr.next
        head = head.next
        return head

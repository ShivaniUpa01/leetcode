"""203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = ListNode(0)
        pre = newHead
        pre.next = head
        curr = head
        while curr != None:
            if curr.val == val:
                pre.next = curr.next
                curr = curr.next
            else:
                pre = curr
                curr = curr.next
        return newHead.next
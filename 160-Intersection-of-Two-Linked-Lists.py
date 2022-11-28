"""Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If
the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

    intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    listA - The first linked list.
    listB - The second linked list.
    skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your
program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the
head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the
intersected node in A; There are 3 nodes before the intersected node in B. - Note that the intersected node's value
is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references.
In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in
A and 4th node in B) point to the same location in memory. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""Solution 1"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        countA = 0
        countB = 0
        if headA == None or headB == None:
            return None
        while a != None:
            a = a.next
            countA += 1
        while b != None:
            b = b.next
            countB += 1
        count = abs(countA - countB)
        a = headA
        b = headB
        if count != 0:
            while count != 0:
                if countA > countB:
                    a = a.next
                    count -= 1
                else:
                    b = b.next
                    count -= 1
        while a != None and b != None:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None

    """Solution 2 """

    class Solution:
        # @param two ListNodes
        # @return the intersected ListNode
        def getIntersectionNode(self, headA, headB):
            if headA is None or headB is None:
                return None

            pa = headA  # 2 pointers
            pb = headB

            while pa is not pb:
                # if either pointer hits the end, switch head and continue the second traversal,
                # if not hit the end, just move on to next
                pa = headB if pa is None else pa.next
                pb = headA if pb is None else pb.next

            return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

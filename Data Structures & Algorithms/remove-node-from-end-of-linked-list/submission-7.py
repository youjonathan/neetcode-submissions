# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # brute force is to keep a count to count total num of nodes
        # then once you reach the end, go to count - n node and edit it

        # how would you increase the efficiency?
        # one way is keeping an array of all nodes?
        # num nodes is constrained to 30 so wouldn't be too costly

        # I'm sure that's not the most optimal method tho...
        # hmmmmmm

        # another possible solution utilizes two pointers
        # how would that work...
        # hint 2: two pass approach
        # i think i tried this earlier but failed
        # let's try again!
        # i'm kind of confused how this is different from the brute force
        # storing in array version, but I'm guessing it doesn't require
        # the extra space?

        # hint 4: two pointers, first one n steps ahead
        first = head
        # for _ in range still messes me up sometimes
        for _ in range(n):
            first = first.next

        second = ListNode()
        second.next = head

        while first:
            first = first.next
            second = second.next
        
        temp = second.next.next
        if temp:
            second.next = temp
        else:
            second.next = None
        
        # how do we handle edge cases in this case?
        # do we still need length?
        
        return head
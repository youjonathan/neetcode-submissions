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
        # checked hint: two pass approach
        # i think i tried this earlier but failed
        # let's try again!
        # i'm kind of confused how this is different from the brute force
        # storing in array version, but I'm guessing it doesn't require
        # the extra space?

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # removing nth node from end = remove N-nth node from front
        remove = length - n + 1

        if remove == 1:
            if length == 1:
                return None
            else:
                return head.next
        
        node = head
        for _ in range(remove - 2):
            node = node.next
        
        temp = node.next.next
        if temp:
            node.next = temp
        else:
            node.next = None
        return head
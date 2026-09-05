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

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        index = count - n
        prev = head
        for i in range(index - 1):
            prev = prev.next
        if prev == head:
            head = head.next

        remove = prev.next
        if not remove:
            return None
        if remove.next:
            change = remove.next
            prev.next = change

        return head
        
        

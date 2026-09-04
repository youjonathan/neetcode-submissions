# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first find the middle so we can split it
        first = head
        second = head

        while second and second.next:
            first = first.next
            second = second.next.next
        
        # print(first.val)

        # next reverse the second half
        prev = None
        curr = first.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        first.next = None

        # merge the two
        head1 = head
        while head2:
            next1 = head1.next
            head1.next = head2
            next2 = head2.next
            head2.next = next1
            head1 = next1
            head2 = next2
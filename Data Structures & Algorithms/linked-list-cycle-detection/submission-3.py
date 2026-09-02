# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # brute force would prob be O(n^2) by just looping through
        # checking if a node is = to any other node's next
        # wait no but when would we know when to stop the while loop?
        
        # two pointers loop
        # so the idea is that if you have one going one at a time
        # and the other going twice the speed
        # if there is a cycle they will eventually intersect
        # but when will it end if they don't intersect?
        # guessing if they get to a null next

        first = head
        second = head

        while first and second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True

        return False
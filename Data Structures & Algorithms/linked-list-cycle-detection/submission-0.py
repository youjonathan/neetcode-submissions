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
        visited = set()

        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False
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

        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        index = len(arr) - n
        if index == 0:
            if len(arr) == 0:
                return None
            else:
                return head.next
        
        prev = arr[index - 1]
        if arr[index + 1]:
            prev.next = arr[index + 1]
        else:
            prev.next = None

        return head
        
        

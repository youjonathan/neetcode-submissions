# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # k can be up to 10000
        # I'm thinking a brute force option is just having one big list
        # and then merge each one individually into that big list
        # this seems extremely inefficient though
        # hm I'm sure the fact that all of these lists
        # are sorted is going to be important somewhere

        # I HAVE NO IDEA
        # looked at the tags, apparently we should use merge sort
        # but that doesn't work super efficiently with the current set up
        # let's just do the brute force version of merge sort
        # that might give us some insight

        arr = []
        for curr in lists:
            while curr:
                arr.append(curr)
                curr = curr.next
        
        arr.sort(key=lambda node: node.val)
        for i, node in enumerate(arr):
            if i + 1 < len(arr):
                next = arr[i + 1]
            else:
                next = None
            node.next = next
        
        return arr[0] if len(arr) > 0 else None
        
        



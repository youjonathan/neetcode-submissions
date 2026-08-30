# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # you have the two lists
        # look at the top of each one, and move the lesser one to the new list
        # move the top of the lists?
        # wire the previous node to this new one
        # repeat

        one = list1
        two = list2

        new_list_head = ListNode()

        new_list_tail = new_list_head

        # repeat until condition?
        # condition is that one or two exist? im a lil confused
        while one and two:
            if one.val < two.val:
                new_list_tail.next = one
                new_list_tail = one
                one = one.next
            else:
                new_list_tail.next = two
                new_list_tail = two
                two = two.next
        
        if one:
            new_list_tail.next = one

        if two:
            new_list_tail.next = two
        
        return new_list_head.next
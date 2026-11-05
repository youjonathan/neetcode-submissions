"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        new_head = Node(head.val)
        hashmap = {head: new_head}

        curr = head
        new_prev = new_head
        while curr.next:
            new_node = Node(curr.next.val)
            hashmap[curr.next] = new_node
            new_prev.next = new_node
            new_prev = new_node
            curr = curr.next

        curr = head
        new_curr = new_head
        while curr:
            if curr.random != None:
                new_curr.random = hashmap[curr.random]
            curr = curr.next
            new_curr = new_curr.next

        return new_head



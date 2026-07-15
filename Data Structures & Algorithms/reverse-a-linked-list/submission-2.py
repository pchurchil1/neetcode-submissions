# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Input: Head, an array of Nodes
    # Each node has a value and a pointer to the next node until the tail
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev


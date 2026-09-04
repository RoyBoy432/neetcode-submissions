# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None; curr = head
        #print(curr.next)
        print(curr)
        while curr:
            ph = curr.next #1 it's the 1 node, the whole thing
            curr.next = prev; print(prev) #set the 1 node to equal None
            prev = curr #set the 
            curr = ph
        return prev
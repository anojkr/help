# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        h = {}
        
        prev = A
        curr = A.next
        
        h[prev.val] = 1
        while(curr!= None):
            if curr.val not in h:
                h[curr.val] = 1
                curr = curr.next
                prev = prev.next
            else:
                t = curr
                curr = curr.next
                prev.next = curr
                
        return A
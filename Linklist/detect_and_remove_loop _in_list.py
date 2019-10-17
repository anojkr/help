# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slow = A
        fast = A
        if A == None:
            return
        
        h = {}
        q = None
        while True:
            if slow not in h:
                h[slow] = 1
                slow = slow.next
            elif slow in h:
                q = slow
                break
 
        p = q
        while True:
            if p is q.next:
                break
            else:
                q = q.next
        q.next= None
        
        return A
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
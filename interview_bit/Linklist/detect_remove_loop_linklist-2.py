# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slow = A.next
        fast = A.next.next
        if A == None:
            return
        
        ptr = None
        
        while (fast!=None and fast.next!= None):
                if slow == fast:
                    ptr = slow
                    break
                slow = slow.next
                fast = fast.next.next
        
        
        if slow != fast:
            return -1
        
        # print(ptr.val)
        t = A
        while True:
            if ptr.next is t.next:
                break
            t = t.next
            ptr = ptr.next
            
        ptr.next = None
        
        return A
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
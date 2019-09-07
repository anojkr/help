# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    h = None
    
    def reverse_list(self, A, B, r):
        curr = A
        prev = None
        nex = None
        count = 0
        
        while (curr != None and count < B and r > 0):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            count +=1
        
        if r == 0:
            return A
        if nex != None:
            A.next = self.reverse_list(nex, B, r-1);
        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        
        t = head
        c = 1
        while (t.next != None):
            t = t.next
            c += 1
            
        r = c//k
        # print(r)
        return self.reverse_list(head, k, r)
        
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
from collections import OrderedDict
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):

        if A == None:
            return
        h = OrderedDict()
        curr = A
        
        while curr != None:
            if curr.val in h:
                h[curr.val]+=1
            elif curr.val not in h:
                h[curr.val] = 1
            curr = curr.next

        temp = None
        ptr = None
        for k,v in h.items():
            if ptr == None and v == 1:
                ptr = ListNode(k)
                temp = ptr
            elif ptr!= None and v==1:
                temp.next = ListNode(k)
                temp = temp.next

        return ptr
            
            
https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/
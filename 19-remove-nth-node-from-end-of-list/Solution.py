# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      ##get size
        # temp = head
        # size = 0 
        # while temp:
        #     size += 1
        #     temp = temp.next
        # if size == 1 and n == 1:
        #     return None
        # idx_to_remove = size - n
        # i = 0
        # if idx_to_remove == 0:
        #     head = head.next
        # previous,current = head,head

        # while current and i!=idx_to_remove:
        #     previous = current
        #     current = current.next
        #     i += 1
        
        # previous.next = current.next
        # return head

        ## better solution that does not require getting size
        ## initialize pointers and left to dummy so we are before removed node
        ## keep a gap of 2 between pointers from the end of the list then remove the node.

        dummy = ListNode(0,head)
        left = dummy 
        right = head

        ## make the gap
        while n > 0:
            right = right.next 
            n -= 1

        ## now shift the gap to the end of the list 
        while right:
            right = right.next
            left = left.next
        
        ## now the 2 pointers are at the correct position we can now delete the node
        left.next = left.next.next
        return dummy.next ##correct head and to remove the dummy node 
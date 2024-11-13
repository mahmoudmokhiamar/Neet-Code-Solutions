# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        while temp and temp.next:
            if temp.val == 0:
                #if last = temp then it won't enter the loop and hence set temp.next to temp hence cycle
                last = temp.next
                current_sum = 0
                while last.val != 0:
                    current_sum += last.val
                    last = last.next
                # Now 'last' is the next zero node or the end of the list
                temp.val = current_sum
                temp.next = last
                if temp.next.next == None:
                    temp.next = None 
            temp = temp.next

        return head
        
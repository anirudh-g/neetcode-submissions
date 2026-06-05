# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force appraoch : convert list to array -> merge , sort -> convert back to list
        l1 = self.convert_list_to_array(l=list1)
        l2 = self.convert_list_to_array(l=list2)

        l1.extend(l2)
        if not l1:
            return None
        
        return self.convert_array_to_list(arr=sorted(l1))
    
    def convert_list_to_array(self, l: Optional[ListNode]):

        arr = []

        while l is not None:
            arr.append(l.val)
            l = l.next
        
        return arr
    
    def convert_array_to_list(self, arr: List):
        head = ListNode(arr[0])
        tail = head

        for val in arr[1:]:
            tail.next = ListNode(val)
            tail = tail.next
        
        return head

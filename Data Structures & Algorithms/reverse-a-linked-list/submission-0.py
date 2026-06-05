# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force approach : convert linkedlist to array -> reverse the array -> then back to LinkedList
        arr = [] 
        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        
        if not arr:
            return None

        arr = arr[::-1]

        head = ListNode(arr[0])
        tail = head

        for val in arr[1:]:
            tail.next = ListNode(val)
            tail = tail.next
        
        return head

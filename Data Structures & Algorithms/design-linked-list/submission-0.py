class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None 

class MyLinkedList:

    def __init__(self):
        # dummy nodes (sentinel nodes) to avoid edge cases
        # these nodes are not part of the linkedlist, but are there to mitigate the edge cases w.r.t add / deleting node
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next

        while curr and index > 0 :
            curr = curr.next
            index-=1
        
        if curr and index == 0 and curr != self.right:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node , next , prev = ListNode(val), self.left.next , self.left

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node, prev , next = ListNode(val) , self.right.prev , self.right

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next 
            index -=1
        
        if curr and index == 0:
            node, prev, next = ListNode(val), curr.prev, curr
            
            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next
        

    def deleteAtIndex(self, index: int) -> None:

        curr = self.left.next

        while curr and index > 0:
            curr = curr.next 
            index -=1
        
        if curr and index == 0 and curr != self.right:
            prev, next = curr.prev, curr.next
            
            prev.next = next
            next.prev = prev
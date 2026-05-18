class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_val = min(val, self.minStack[-1]) if self.minStack  else val
        self.minStack.append(current_val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # since min(self.stack) scans the entire stack everytime, it will be O(n) not O(1)
        # Since we need an O(1) solution as per the criteria here :
        # Therfore, use a two-stack approach where one is regular stack and other in minStack to track the minimum val before inserting.
        # if its the minVal up until that point, then insert it into the minStack.
        # When popping, pop both the regular and minStack
        # so, when getting the minStack up until that point, only returning the last element is enough as it will be an O(1) operation
        return self.minStack[-1]

        

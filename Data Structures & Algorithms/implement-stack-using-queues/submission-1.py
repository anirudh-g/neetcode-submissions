class MyStack:
    '''
    deque are double-ended queues. 
    ue them with self-imposed constraint of using it like a stack
    '''
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft()) # rotate front elements to back . rotate() function rotates back elements to front , hence this implemented approach

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
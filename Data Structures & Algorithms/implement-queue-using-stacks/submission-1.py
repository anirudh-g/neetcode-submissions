class MyQueue:

    def __init__(self):
        self.first_stack = []
        self.aux_stack = []

    def push(self, x: int) -> None:
        self.first_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.aux_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.aux_stack[-1]

    def empty(self) -> bool:
        return not self.first_stack and not self.aux_stack

    def _move(self):
        # transfer elements only when needed
        # lazy transfer elements to aux_stack only when its empty
        if not self.aux_stack:
            while self.first_stack:
                self.aux_stack.append(self.first_stack.pop())
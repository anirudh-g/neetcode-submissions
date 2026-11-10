class Solution:
    def minOperations(self, logs: List[str]) -> int:
        '''
        Using stack here is also valid, but that means
        we need to scan the stack to get the length.

        the problem asks for only the depth i.e no.of moves to go back to root , not the list of folders. Therefore, 
        a simple counter approach would be efficient here.
        '''
        depth = 0

        for i in logs:
            if i == './':
                continue
            elif i == '../':
                if depth > 0:
                    depth-=1
            else:
                depth +=1
        return depth
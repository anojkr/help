class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack = []
        self.m = []


    def push(self, x):
        self.stack.append(x)
        if len(self.m) == 0:
            self.m.append(x)
        else:
            if self.stack[-1] <= self.m[-1]:
                self.m.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            if len(self.m) > 0 and self.stack[-1] == self.m[-1]:
                self.stack.pop()
                self.m.pop()
            else:
                self.stack.pop()


    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1
        
    # @return an integer
    def getMin(self):
        if len(self.m) > 0:
            return self.m[-1]
        return -1

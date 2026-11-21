class MinStack:

    def __init__(self):
        self.stack = []   # the plates
        self.mins = []    # one note per plate: smallest so far

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:                              # first plate: it IS the smallest
            self.mins.append(val)
        else:                                          # smaller of this plate and the note below
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.stack.pop()      # the plate goes
        self.mins.pop()       # and its note goes with it

    def top(self) -> int:
        return self.stack[-1]     # top plate

    def getMin(self) -> int:
        return self.mins[-1]      # top note
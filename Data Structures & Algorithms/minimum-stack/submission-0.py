class MinStack:

    def __init__(self):
        self.storage = []
        self.min_storage = []

    def push(self, val: int) -> None:
        
        if not self.storage:
            self.storage.append(val)
            self.min_storage.append(val)
        else:
            self.storage.append(val)
            self.min_storage.append(min(val, self.min_storage[-1]))

    def pop(self) -> None:
        self.storage.pop()
        self.min_storage.pop()

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return self.min_storage[-1]        

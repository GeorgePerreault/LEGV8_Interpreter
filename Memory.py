class MemoryException(Exception):
    pass

class Memory:

    def __init__(self, bounds=0xFFFFFFFFFFFFFFFF):
        self.memory = {}
        self.bounds = bounds

    def __getitem__(self, i):
        if i > self.bounds:
            raise MemoryException(f"Address {i} is out of bounds")
        return self.memory[i]

    def __setitem__(self, i, v):
        if i > self.bounds:
            raise MemoryException(f"Address {i} is out of bounds")
        self.memory[i] = v
class Memory:

    # A dictionary is used to mimic an array of size 2^64
    def __init__(self, bounds=0xFFFFFFFFFFFFFFFF):
        self.memory = {}
        self.bounds = bounds

    def __repr__(self):
        return str(self.memory)

    def __getitem__(self, i):
        if i > self.bounds or i < 0:
            raise IndexError(f"Address {i} is out of bounds")
        return self.memory[i]

    def __setitem__(self, i, v):
        if i > self.bounds or i < 0:
            raise IndexError(f"Address {i} is out of bounds")
        self.memory[i] = v
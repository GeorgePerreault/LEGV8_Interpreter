from src.UsefulFuncs import num_as_str

class Memory:

    # A dictionary is used to mimic an array of size 2^64
    def __init__(self, bounds=0xFFFFFFFFFFFFFFFF):
        self.memory = {}
        self.bounds = bounds

    def print(self, address=None, mode="dec"):
        if address:
            self.__single_print(address, mode)
        else:
            for i in sorted(self.memory.keys()):
                self.__single_print(mode, i)
    
    def __single_print(self, address, mode):
        print(f"{num_as_str(address, mode)}: {self.memory[address]}")
            
    def __repr__(self):
        return str(self.memory)

    def __getitem__(self, i):
        if i > self.bounds or i < 0:
            raise IndexError(f"Address {i} is out of bounds")
        try:
            ret = self.memory[i]
        except KeyError:
            return 0
        return ret

    def __setitem__(self, i, v):
        if i > self.bounds or i < 0:
            raise IndexError(f"Address {i} is out of bounds")
        self.memory[i] = v
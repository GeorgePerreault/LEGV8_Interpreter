from src.UsefulFuncs import num_as_str
from src.BitNumber import BitNumber

class Memory:

    # A dictionary is used to mimic an array of size 2^64
    def __init__(self, bounds=0xFFFFFFFFFFFFFFFF):
        self.memory = {}
        self.bounds = bounds

    def print(self, address=None, mode="dec"):
        if address:
            self.__single_print(address, mode)
        else:
            for i in sorted(i for i in self.memory.keys() if i % 8 == 0):
                self.__single_print(BitNumber(i), mode)
    
    def __single_print(self, address, mode):
        str_address = num_as_str(address.bits, mode)
        value = self.load_bytes(address, 8).bits
        str_value = num_as_str(value, mode)
        
        print(f"{str_address}: {str_value}")
    
    def load_bytes(self, start, n_bytes):
        res = BitNumber()
        start = int(start)

        for i in range(start, start + n_bytes - 1):
            res |= self[i]
            res <<= 8

        # Last bitwise or is outside to avoid left shifting too much 
        res |= self[start + n_bytes - 1]
        return res


    def store_bytes(self, val, start, n_bytes):
        start = int(start)

        # Store stores in reverse to make loading easier
        for i in range(start, start + n_bytes)[::-1]:
            self[i] = val & 0xFF
            val >>= 8


    def __repr__(self):
        return str([f"{i}: {self.memory[i]}" for i in sorted(self.memory)])

    def __getitem__(self, i):
        if i > self.bounds or i < 0:
            raise IndexError(f"Address {i} is out of bounds")
        try:
            ret = self.memory[i]
        except KeyError:
            return BitNumber(0)
        return ret

    def __setitem__(self, i, v):
        if i > self.bounds or i < 0:
            raise IndexError(f"Address {i} is out of bounds")
        self.memory[i] = v
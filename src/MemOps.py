from src.Op import Op
from src.BitNumber import BitNumber


class Load(Op):

    def execute(self, x, y, z):
        memory = self.cpu.memory

        res = BitNumber()
        low = int(y + z)
        
        for i in range(low, low + self.n_bytes - 1):
            res |= memory[i]
            res <<= 8

        # Last bitwise or is outside to avoid left shifting too much 
        res |= memory[low + self.n_bytes - 1]

        x.assign(res)
        return res


class Store(Op):

    def execute(self, x, y, z):
        memory = self.cpu.memory

        val = x.value
        low = int(y + z)

        # Store stores in reverse to make loading easier
        for i in range(low, low + self.n_bytes)[::-1]:
            memory[i] = val & 0xFF
            val >>= 8

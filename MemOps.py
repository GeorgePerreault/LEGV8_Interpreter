from BitNumber import BitNumber

class MemOp():

    def __init__(self, cpu, n_bytes=8):
        self.memory = cpu.memory
        self.n_bytes = n_bytes


class Load(MemOp):

    def execute(self, x, y, z):
        res = BitNumber()
        low = int(y + z)
        
        for i in range(low, low + self.n_bytes - 1):
            res |= self.memory[i]
            res <<= 8
        res |= self.memory[low + self.n_bytes - 1]

        x.assign(res)
        return res


class Store(MemOp):

    def execute(self, x, y, z):
        val = x.value
        low = int(y + z)

        for i in range(low, low + self.n_bytes)[::-1]:
            self.memory[i] = val & 0xFF
            val >>= 8

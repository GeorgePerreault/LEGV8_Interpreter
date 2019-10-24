from code.Op import Op
from code.BitNumber import BitNumber


class Load(Op):

    def execute(self, x, y, z):
        memory = self.cpu.memory

        res = BitNumber()
        low = int(y + z)
        
        for i in range(low, low + self.n_bytes - 1):
            res |= memory[i]
            res <<= 8
        res |= memory[low + self.n_bytes - 1]

        x.assign(res)
        return res


class Store(Op):

    def execute(self, x, y, z):
        memory = self.cpu.memory

        val = x.value
        low = int(y + z)

        for i in range(low, low + self.n_bytes)[::-1]:
            memory[i] = val & 0xFF
            val >>= 8

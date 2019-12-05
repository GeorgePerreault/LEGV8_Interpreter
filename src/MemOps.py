from src.Op import Op
from src.BitNumber import BitNumber


class Load(Op):

    def execute(self, x, y, z):
        start = y + z
        res = self.cpu.memory.load_bytes(start, self.n_bytes)
        x.assign(res)

        return res


class Store(Op):

    def execute(self, x, y, z):
        val = x.value
        start = y + z
        self.cpu.memory.store_bytes(val, start, self.n_bytes)


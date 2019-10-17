
class MathOp():

    def __init__(self, cpu, s=False):
        self.cpu = cpu
        self.s = s

class Add(MathOp):

    def execute(self, x, y, z):
        res = y + z
        x.assign(res)
        if self.s:
            self.cpu.set_flags()
        return res

class Sub(MathOp):

    def execute(self, x, y, z):
        res = y - z
        x.assign(res)
        if self.s:
            self.cpu.set_flags()
        return res

class And():
    def execute(self, x, y, z):
        x.assign(y & z)

class Or():
    def execute(self, x, y, z):
        x.assign(y | z)

class Eor():
    def execute(self, x, y, z):
        x.assign(y ^ z)
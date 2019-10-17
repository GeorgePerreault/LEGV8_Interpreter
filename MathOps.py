
class MathOp():

    def __init__(self, cpu, s=False):
        self.cpu = cpu
        self.s = s

    def get_flags(self):
        pass

class Add(MathOp):

    def execute(self, x, y, z):
        x.assign(y + z)
        if self.s:
            self.cpu.set_flags(self.get_flags())

class Sub(MathOp):

    def execute(self, x, y, z):
        x.assign(y - z)

class MathOp():

    def __init__(self, s=False):
        self.s = s

class Add(MathOp):

    def execute(self, x, y, z):
        res = y + z
        x.assign(res)
        return res

class Sub(MathOp):

    def execute(self, x, y, z):
        res = y - z
        x.assign(res)
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
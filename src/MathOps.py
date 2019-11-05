from src.Op import Op

class Add(Op):
    def execute(self, x, y, z):
        if self.s:
            res, flags = y.__add__(z, give_flags=True)
            x.assign(res)
            return res, flags
        else:
            res = y + z
            x.assign(res)
            return res

class Sub(Op):
    def execute(self, x, y, z):
        if self.s:
            res, flags = y.__sub__(z, give_flags=True)
            x.assign(res)
            return res, flags
        else:
            res = y - z
            x.assign(res)
            return res

class And(Op):
    def execute(self, x, y, z):
        x.assign(y & z)

class Or(Op):
    def execute(self, x, y, z):
        x.assign(y | z)

class Eor(Op):
    def execute(self, x, y, z):
        x.assign(y ^ z)

class LeftShift(Op):
    def execute(self, x, y, z):
        x.assign(y.value << z)

class RightShift(Op):
    def execute(self, x, y, z):
        x.assign(y.value >> z)
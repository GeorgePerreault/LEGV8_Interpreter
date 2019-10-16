
class MathOp():

    def __init__(self, i=False, s=False):
        self.i = i
        self.s = s

class Add(MathOp):

    def execute(self, x, y, z):
        x.assign(y + z)


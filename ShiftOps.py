class LeftShift():

    def execute(self, x, y, z):
        x.assign(y.value << z)

class RightShift():

    def execute(self, x, y, z):
        x.assign(y.value >> z)
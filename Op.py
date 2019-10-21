class Op():

    def __init__(self):
        self.cpu = None

    def __call__(self, cpu):
        self.cpu = cpu
        return self
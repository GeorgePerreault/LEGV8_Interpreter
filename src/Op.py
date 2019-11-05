class Op():

    def __init__(self, s=False, n_bytes=8):
        self.cpu = None
        self.s = s
        self.n_bytes = n_bytes

    def __call__(self, cpu):
        self.cpu = cpu
        return self
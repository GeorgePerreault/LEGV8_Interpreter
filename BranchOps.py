class BranchOp():

    def __init__(self, cpu, condition=None):
        self.cpu = cpu
        self.conditon = condition


class Branch(BranchOp):

    def execute(self, goto, *params):
        if self.conditon:
            if not self.conditon(*params):
                return False

        self.cpu.ip = goto
        return True
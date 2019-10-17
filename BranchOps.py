class BranchOp():

    def __init__(self, cpu, condition=lambda : True):
        self.cpu = cpu
        self.condition = condition

    def branch_on(self, *params):
        return self.condition(*params)

    def execute(self, goto, *params):
        if self.branch_on(*params):
            self.cpu.ip = goto



class BranchEQ(BranchOp):
    def branch_on(self):
        return True

class BranchNE(BranchOp):
    def branch_on(self):
        return True

class BranchHS(BranchOp):
    def branch_on(self):
        return True

class BranchLO(BranchOp):
    def branch_on(self):
        return True

class BranchMI(BranchOp):
    def branch_on(self):
        return True

class BranchPL(BranchOp):
    def branch_on(self):
        return True

class BranchVS(BranchOp):
    def branch_on(self):
        return True

class BranchHI(BranchOp):
    def branch_on(self):
        return True

class BranchLS(BranchOp):
    def branch_on(self):
        return True

class BranchGE(BranchOp):
    def branch_on(self):
        return True

class BranchLT(BranchOp):
    def branch_on(self):
        return True

class BranchGT(BranchOp):
    def branch_on(self):
        return True

class BranchLE(BranchOp):
    def branch_on(self):
        return True
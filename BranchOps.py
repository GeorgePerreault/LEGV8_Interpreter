class BranchOp():

    def __init__(self, cpu):
        self.cpu = cpu

    def branch_on(self):
        return True

    def execute(self, goto):
        if self.branch_on():
            self.cpu.ip = goto

class CondBranch(BranchOp):

    def __init__(self, cpu, condition=None):
        self.cpu = cpu
        self.condition = condition

    def execute(self, goto, reg):
        if self.condition(reg):
            self.cpu.ip = int(reg.value)

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
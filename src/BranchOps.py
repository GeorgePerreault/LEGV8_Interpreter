from src.Op import Op

class BranchOp(Op):
    def branch_on(self):
        return True

    def execute(self, goto):
        if self.branch_on():
            self.cpu.pc = goto

class CondBranch(BranchOp):
    def __init__(self, condition=None):
        super().__init__()
        self.condition = condition

    def execute(self, reg, goto):
        if self.condition(reg):
            self.cpu.pc = goto

class BranchLink(BranchOp):
    def execute(self, goto):
        # 30 is the link register
        self.cpu.registers[30].assign(self.cpu.pc)
        self.cpu.pc = goto

class BranchReg(BranchOp):    
    def execute(self, goto_reg):
        self.cpu.pc = int(goto_reg.value)

# The following checks for each branch were pulled from a slide

class BranchEQ(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.zero == 1

class BranchNE(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.zero == 0

class BranchHS(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.carry == 1

class BranchLO(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.carry == 0

class BranchMI(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.negative == 1

class BranchPL(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.negative == 0

class BranchVS(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.overflow == 1

class BranchVC(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.overflow == 0

class BranchHI(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.carry == 1 and self.cpu.saved_flags.zero == 0

class BranchLS(BranchOp):
    def branch_on(self):
        return not (self.cpu.saved_flags.carry == 1 and self.cpu.saved_flags.zero == 0)

class BranchGE(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.negative == self.cpu.saved_flags.overflow

class BranchLT(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.negative != self.cpu.saved_flags.overflow

class BranchGT(BranchOp):
    def branch_on(self):
        return self.cpu.saved_flags.zero == 0 and self.cpu.saved_flags.negative == self.cpu.saved_flags.overflow

class BranchLE(BranchOp):
    def branch_on(self):
        return not (self.cpu.saved_flags.zero == 0 and self.cpu.saved_flags.negative == self.cpu.saved_flags.overflow)
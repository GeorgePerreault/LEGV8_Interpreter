from MathOps import Add
from MemOps import Load, Store
from BranchOps import Branch

class OpcodeTable():

    def __init__(self, cpu):
        self.OPCODE_TABLE = {
            "add": Add(),
            "addi": Add(i=True),
            "adds": Add(s=True),
            "addis": Add(i=True, s=True),
            "ldur": Load(cpu),
            "ldurw": Load(cpu, n_bytes=4),
            "ldurh": Load(cpu, n_bytes=2),
            "ldurb": Load(cpu, n_bytes=1),
            "stur": Store(cpu),
            "sturw": Store(cpu, n_bytes=4),
            "sturh": Store(cpu, n_bytes=2),
            "sturb": Store(cpu, n_bytes=1),
            "b": Branch(cpu)
        }

    def __getitem__(self, i):
        return self.OPCODE_TABLE[i]

    def __setitem__(self, i, v):
        raise Exception("Don't set item on the opcode table")
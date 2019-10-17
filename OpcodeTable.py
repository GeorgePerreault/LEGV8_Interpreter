from MathOps import Add, Sub, And, Or, Eor
from MemOps import Load, Store
from BranchOps import Branch
from ShiftOps import LeftShift, RightShift

class OpcodeTable():

    def __init__(self, cpu):
        self.OPCODE_TABLE = {
            "add": Add(cpu),
            "addi": Add(cpu),
            "adds": Add(cpu, s=True),
            "addis": Add(cpu, s=True),

            "sub": Sub(cpu),
            "subi": Sub(cpu),
            "subs": Sub(cpu, s=True),
            "subis": Sub(cpu, s=True),

            "and": And(),
            "andi": And(),

            "or": Or(),
            "ori": Or(),

            "eor": Eor(),
            "eori": Eor(),

            "lsl": LeftShift(),
            "lsr": RightShift(),

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
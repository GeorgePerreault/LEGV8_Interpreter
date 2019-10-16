from MathOps import Add
from MemOps import Load, Store

class OpcodeTable():

    def __init__(self, memory):
        self.OPCODE_TABLE = {
            "add": Add(),
            "addi": Add(i=True),
            "adds": Add(s=True),
            "addis": Add(i=True, s=True),
            "ldur": Load(memory),
            "ldurw": Load(memory, n_bytes=4),
            "ldurh": Load(memory, n_bytes=2),
            "ldurb": Load(memory, n_bytes=1),
            "stur": Store(memory),
            "sturw": Store(memory, n_bytes=4),
            "sturh": Store(memory, n_bytes=2),
            "sturb": Store(memory, n_bytes=1),
        }

    def __getitem__(self, i):
        return self.OPCODE_TABLE[i]

    def __setitem__(self, i, v):
        raise Exception("Don't set item on the opcode table")
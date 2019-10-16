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
            "stur": Store(memory) 
        }

    def __getitem__(self, i):
        return self.OPCODE_TABLE[i]

    def __setitem__(self, i, v):
        raise Exception("Don't set item on the opcode table")
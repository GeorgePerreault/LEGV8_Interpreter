from Register import Register
from Instruction import Instruction
from Token import REGISTER, IMMEDIATE

class CPU:


    def __init__(self):
        self.registers = [Register(i) for i in range(32)]
        self.params = None
        self.func = None
        self.ip = 0

        self.OPCODE_TABLE = {
            "add": self.op_add,
            "addi": self.op_add
        }


    def decode(self, instruction: Instruction):
        self.params = []

        for i in instruction.params:
            if i.type == REGISTER:
                self.params.append(self.registers[i.r_number])
            elif i.type == IMMEDIATE:
                self.params.append(i.i_val)

        self.func = self.OPCODE_TABLE[instruction.opcode]

    def execute(self):
        self.func(*self.params)
        self.ip += 1

    def op_add(self, x, y, z):
        x.assign(y + z)

    def __repr__(self):
        return str(self.registers)
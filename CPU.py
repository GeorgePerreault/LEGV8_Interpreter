from Register import Register
from Instruction import Instruction
from Memory import Memory
from Token import REGISTER, IMMEDIATE

class CPU:


    def __init__(self):
        self.registers = [Register(i) for i in range(32)]
        self.params = None
        self.func = None
        self.ip = 0

        self.memory = Memory()

        self.OPCODE_TABLE = {
            "add": self.op_add,
            "addi": self.op_add,
            "ldur": self.op_load_8,
            "stur": self.op_store_8
        }


    def decode(self, instruction: Instruction):
        self.params = []

        for i in instruction.params:
            if i.type == REGISTER:
                self.params.append(self.registers[i.r_val])
            elif i.type == IMMEDIATE:
                self.params.append(i.i_val)

        self.func = self.OPCODE_TABLE[instruction.opcode]

    def execute(self):
        self.func(*self.params)
        self.ip += 1

    def op_add(self, x, y, z):
        x.assign(y + z)
    
    def op_load(self, x, y, z, n):
        res = 0
        for i in range(y + z, y + z + n):
            res |= self.memory[i]
            print(i)
            res <<= 8
        x.assign(res)

    def op_store(self, x, y, z, n):
        res = x.value
        for i in range(y + z, y + z + n):
            self.memory[i] = n & 0xFF
            res >>= 8

    def op_load_8(self, x, y, z):
        self.op_load(x, y, z, 8)

    def op_store_8(self, x, y, z):
        self.op_store(x, y, z, 8)

    def __repr__(self):
        return str(self.registers)
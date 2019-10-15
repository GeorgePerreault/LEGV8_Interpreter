from Register import Register
from Instruction import Instruction
from Token import REGISTER

class CPU:
    def __init__(self):
        self.registers = [Register(i) for i in range(32)]

    def set_registers(self, instruction: Instruction):
        instruction.params = ((i if i.type != REGISTER else self.registers[i.r_number]) for i in instruction.params)

    def execute(self, instruction: Instruction):
        f = instruction.func
        f(*instruction.params)

    def __repr__(self):
        return str(self.registers)
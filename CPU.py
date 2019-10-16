from Register import Register
from Instruction import Instruction
from Memory import Memory
from Token import REGISTER, IMMEDIATE

class CPU:


    def __init__(self):
        self.registers = [Register(i) for i in range(32)] #ALERT: Hardcoded number of registers
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
        low = y + z
        
        for i in range(low, low + n - 1):
            res |= self.memory[i]
            res <<= 8
        res |= self.memory[low + n - 1]
        x.assign(res)

    def op_store(self, x, y, z, n):
        val = x.value
        low = y + z

        for i in range(low, low + n)[::-1]:
            self.memory[i] = val & 0xFF
            val >>= 8

    def op_load_8(self, x, y, z):
        self.op_load(x, y, z, 8)

    def op_store_8(self, x, y, z):
        self.op_store(x, y, z, 8)

    def reg_dump(self, mode="dec", row_size=4):
        i = 0
        row_counter = 0
        s = ""

        while i < len(self.registers):
            c_reg = self.registers[i]

            s += f"X{c_reg.number:02}: "
            if mode == "dec":
                s += f"{c_reg.value:010}"
            elif mode == "hex":
                s += f"{c_reg.value:08x}"
            elif mode == "bin":
                s += f"{c_reg.value:032b}"

            row_counter += 1
            i += 1

            if row_counter == row_size:
                row_counter = 0
                s += "\n"
            else:
                s += "\t"

        print(s)
            

    def __repr__(self):
        return str(self.registers)
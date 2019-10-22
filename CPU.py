from Register import Register, special_reg_names
from Instruction import Instruction
from Memory import Memory
from InstructionSet import INSTRUCTION_SET, TTS, FUNC
from Flags import Flags
from MathOps import Add, Sub

class CPU:

    def __init__(self):
        self.registers = [Register(i) for i in range(32)] #ALERT: Hardcoded number of registers
        self.params = None
        self.op = None
        self.pc = 1

        self.tmp_flags = Flags()
        self.saved_flags = Flags()

        self.memory = Memory()

    def set_flags(self):
        self.saved_flags.set_flags(self.tmp_flags)
    
    def decode(self, instruction, labels):
        if not instruction.opcode:
            self.params = None
            self.op = None
            return
        self.params = []

        for i in instruction.params:
            if i.type == TTS.REGISTER:
                self.params.append(self.registers[i.r_val])
            elif i.type == TTS.IMMEDIATE:
                self.params.append(i.i_val)
            elif i.type == TTS.LABEL:
                try:
                    goto = labels[i.l_val]
                except KeyError:
                    raise KeyError(f"Invalid label: {i.l_val}")
                self.params.append(goto)

        self.op = INSTRUCTION_SET[instruction.opcode][FUNC](self)

    def execute(self):
        self.pc += 1

        if not self.op:
            return

        ret = self.op.execute(*self.params)
        
        if ret:
            self.tmp_flags.carry = ret.carry
            self.tmp_flags.overflow = ret.overflow
            self.tmp_flags.negative = ret.negative
            self.tmp_flags.zero = ret.zero

        if type(self.op) is Add or type(self.op) is Sub:
            if self.op.s:
                self.set_flags()
    
    def reg_dump(self, mode="dec", row_size=4):
        row_counter = 0
        s = ""

        for reg in self.registers:
            s += reg.__repr__(mode=mode)

            row_counter += 1

            if row_counter == row_size:
                row_counter = 0
                s += "\n"
            else:
                s += "\t"

        print(s)
            

    def __repr__(self):
        return str(self.registers)
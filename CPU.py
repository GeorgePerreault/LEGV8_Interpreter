from Register import Register
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
        self.ip = 0

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
        self.ip += 1

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
        i = 0
        row_counter = 0
        s = ""

        while i < len(self.registers):
            c_reg = self.registers[i]

            s += f"X{c_reg.number:02}: "
            if mode == "dec":
                s += f"{c_reg.value.bits:020}"
            elif mode == "hex":
                s += f"0x{c_reg.value.bits:016x}"
            elif mode == "bin":
                s += f"0b{c_reg.value.bits:064b}"

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
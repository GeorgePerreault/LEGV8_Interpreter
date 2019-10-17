from Register import Register
from Instruction import Instruction
from Memory import Memory
from InstructionSet import TTS
from OpcodeTable import OpcodeTable

class CPU:


    def __init__(self):
        self.registers = [Register(i) for i in range(32)] #ALERT: Hardcoded number of registers
        self.params = None
        self.op = None
        self.ip = 0

        self.memory = Memory()
        self.OPCODE_TABLE = OpcodeTable(self)

    def decode(self, instruction: Instruction, labels):
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

        self.op = self.OPCODE_TABLE[instruction.opcode]

    def execute(self):
        self.ip += 1
        self.op.execute(*self.params)
    
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
                s += f"0x{c_reg.value:08x}"
            elif mode == "bin":
                s += f"0b{c_reg.value:032b}"

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
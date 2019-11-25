from src.Register import Register, special_reg_names
from src.Instruction import Instruction
from src.Memory import Memory
from src.InstructionSet import INSTRUCTION_SET, TTS, FUNC
from src.Flags import Flags
from src.MathOps import Add, Sub
from src.Exceptions import ExecutionError

class CPU:

    def __init__(self, pc=1):
        self.registers = [Register(i) for i in range(32)]
        self.params = None
        self.op = None
        self.pc = pc

        self.saved_flags = Flags()
        self.memory = Memory()

    def set_flags(self, flags):
        self.saved_flags.set_flags(flags)
    
    # Readies an instruction to be executed
    def decode(self, instruction, labels):
        # This is for if the instruction is just a label
        if not instruction.opcode:
            self.params = None
            self.op = None
            return

        # Changing the tokens into usable values 
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
                    raise ExecutionError(f"Invalid label: {i.l_val}")
                self.params.append(goto)

        self.op = INSTRUCTION_SET[instruction.opcode][FUNC](self)

    def execute(self):
        # pc inc is done before execution to not mess up jumps
        self.pc += 1

        if not self.op:
            return

        ret = self.op.execute(*self.params)
        
        # op.s says if it was a set flag instruction
        # ret should always exist if true but I check anyway
        if self.op.s and ret:
            self.set_flags(ret)

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
            
    def mem_dump(self):
        print(self.memory)

    def __repr__(self):
        return str(self.registers)
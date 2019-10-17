from InstructionSet import TTS

class Instruction:
    
    def __init__(self, opcode, params, label=None):
        self.opcode = opcode
        self.params = params
        self.label = label
        self.set_flags = True if self.opcode[-1] == "s" else False

    def build_str(self):
        s = f"{self.opcode} "

        for param in self.params:
            s += f"{param}"
            if param.type == TTS.COMMA:
                s += " "
        return s

    def __repr__(self):
        return self.build_str()

from InstructionSet import TTS

class Instruction:
    
    def __init__(self, opcode, params, label=None):
        self.opcode = opcode
        self.params = params
        self.label = label

    def build_str(self):
        if not self.opcode:
            return ""
        
        s = f"{self.opcode} "

        for param in self.params:
            s += f"{param}"
            if param.type == TTS.COMMA:
                s += " "
        return s

    def __repr__(self):
        return self.build_str()

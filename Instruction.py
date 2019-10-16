from Token import OPEN_SQUARE, CLOSE_SQUARE

class Instruction:
    
    def __init__(self, opcode, params, label=None):
        self.opcode = opcode
        self.params = params
        self.label = label
        self.set_flags = True if self.opcode[-1] == "s" else False

    def build_str(self):
        s = f"{self.opcode} "

        for param in self.params:
            if param.type == OPEN_SQUARE:
                s += f"{param}"
            elif param.type == CLOSE_SQUARE:
                s = s[:-2]
                s += f"{param}  "
            else:
                s += f"{param}, "
        return s[:-2]

    def __repr__(self):
        try:
            return self.build_str()
        except IndexError:
            return f"{self.opcode} {self.params}"
class Instruction:
    
    def __init__(self, opcode, params):
        self.opcode = opcode
        self.params = params
        self.set_flags = True if self.opcode[-1] == "s" else False
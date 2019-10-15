class Instruction:
    
    def __init__(self, opcode, params, func):
        self.opcode = opcode
        self.params = params
        self.func = func
        self.set_flags = True if self.opcode[-1] == "s" else False
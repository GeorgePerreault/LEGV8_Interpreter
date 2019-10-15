from Instruction import Instruction
from Token import Token
from instruction_set import INSTRUCTION_SET

class ParserException(Exception):
    pass

class LexicalAnalyzer:
    def __init__(self, file):
        self.file = open(file, "r")
        self.die = False

    def get_instruction(self):
        line = self.file.readline()
        if line == "":
            return None

        n = line.find(" ")
        opcode = line[:n]
        line = line[n:].replace(" ", "").strip()
        
        params = []
        s = ""
        for (i, c) in enumerate(line):
            
            if c == "]":
                params.append(Token(s))
                params.append(Token(c))
                s = ""
                continue
            
            if c == "[":
                params.append(Token(c))
                continue

            if c == "," or i == len(line) - 1:
                params.append(Token(s))
                s = ""
                continue

            s += c


        try:
            guideline = INSTRUCTION_SET[opcode]
        except KeyError:
            raise ParserException(f"Invalid opcode: {opcode}")
        
        for (param, guide) in zip(params, guideline):
            if param.type != guide:
                raise ParserException(f"Invalid parameters for '{opcode}': {params}")
        return Instruction(opcode, params)

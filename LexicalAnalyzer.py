from Instruction import Instruction
from Token import Token
from instruction_set import INSTRUCTION_SET

class LexicalAnalyzer:
    def __init__(self, file):
        pass

    def get_instruction(self):
        return Instruction("addi", (Token("X0"), Token("X1"), Token("#69")))

    def get_token(self):
        pass
from string import ascii_letters
from Instruction import Instruction
from Token import Token, REGISTER, IMMEDIATE, LABEL, OPEN_SQUARE, CLOSE_SQUARE, REGISTER_NC, IMMEDIATE_NH
from InstructionSet import INSTRUCTION_SET

ALLOWED_CHARS = {*ascii_letters, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

class ParserError(Exception):
    pass

class LexicalAnalyzer:
    def __init__(self, file):
        self.file = open(file, "r")
        self.cur_pos = 0
        self.cur_line = ""
        self.cur_label = ""
        self.has_label = False

    def get_label(self):
        if not self.has_label:
            raise Exception("Tried to get non-existent label")
        self.has_label = False
        return self.cur_label

    def set_label(self, label):
        if self.has_label:
            raise Exception("Overwrote existing label")
        self.has_label = True
        self.cur_label = label

    def get_str(self):
        s = ""
        while self.cur_pos < len(self.cur_line) and self.cur_line[self.cur_pos] in ALLOWED_CHARS:
            s += self.cur_line[self.cur_pos]
            self.cur_pos += 1
        return s

    def get_one(self):
        if self.cur_pos >= len(self.cur_line):
            return ""
        self.cur_pos += 1
        return self.cur_line[self.cur_pos - 1]

    def error_check(self, match):
        if self.cur_line[self.cur_pos] != match:
            raise ParserError(f"Invalid syntax at: {self.cur_line}. Expected: '{match}' but got {self.cur_line[self.cur_pos]}")
        self.cur_pos += 1

    
    def get_opcode(self):
        opcode = self.get_str()
        print(opcode)
        if self.cur_line[self.cur_pos] == ":": #Not an opcode was actually a label
            self.set_label(opcode)
            self.cur_pos += 1

            self.error_check(" ")
            opcode = self.get_str()

        return opcode


    def get_params(self, expected_params):
        params = []
        s = ""
        for expec in expected_params:
            if expec == REGISTER:
                t = Token(self.get_str())
                if t.type != REGISTER:
                    raise ParserError(f"Expected register but got: {t}")

                params.append(t)
                self.error_check(",")
                self.error_check(" ")

            if expec == REGISTER_NC:
                t = Token(self.get_str())
                if t.type != REGISTER:
                    raise ParserError(f"Expected register but got: {t}")

                params.append(t)


            elif expec == IMMEDIATE:
                self.error_check("#")

                t = Token(self.get_str())
                if t.type != IMMEDIATE:
                    raise ParserError(f"Expected immediate but got: {t}")

                params.append(t)

            elif expec == LABEL:
                t = Token(self.get_str())
                if t.type != LABEL:
                    raise ParserError(f"Expected label but got: {t}")

                params.append(t)

            elif expec == OPEN_SQUARE:
                t = Token(self.get_one())
                if t.type != OPEN_SQUARE:
                    raise ParserError(f"Expected open square-bracket but got: {t}")

                params.append(t)

            elif expec == CLOSE_SQUARE:
                t = Token(self.get_one())
                if t.type != CLOSE_SQUARE:
                    raise ParserError(f"Expected close square-bracket but got: {t}")

                params.append(t)

        return params

    def get_instruction(self):
        self.cur_line = " ".join(self.file.readline().split())
        self.cur_pos = 0

        if self.cur_line == "":
            return None

        opcode = self.get_opcode()

        try:
            expected_params = INSTRUCTION_SET[opcode]
        except KeyError:
            raise ParserError(f"Invalid opcode: {opcode}")


        self.error_check(" ")

        params = self.get_params(expected_params)
        
        if self.has_label:
            return Instruction(opcode, params, label=self.cur_label)
        return Instruction(opcode, params)

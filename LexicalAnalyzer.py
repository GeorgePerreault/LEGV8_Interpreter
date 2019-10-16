from string import ascii_letters
from Instruction import Instruction
from Token import Token
from instruction_set import INSTRUCTION_SET

ALLOWED_CHARS = {*ascii_letters, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "#"}

class ParserException(Exception):
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

    def error_check(self, match):
        if self.cur_line[self.cur_pos] != match:
            raise ParserException(f"Invalid syntax at: {self.cur_line}. Expected {match} but got {self.cur_line[self.cur_pos]}")


    def get_instruction(self):
        self.cur_line = " ".join(self.file.readline().split())
        self.cur_pos = 0

        if self.cur_line == "":
            return None

        opcode = self.get_str()

        if self.cur_line[self.cur_pos] == ":": #Not an opcode was actually a label
            self.set_label(opcode)

            self.cur_pos += 1

            self.error_check(" ")
            self.cur_pos += 1

            opcode = self.get_str()

        try:
            expected_params = INSTRUCTION_SET[opcode]
        except KeyError:
            raise ParserException(f"Invalid opcode: {opcode}")


        self.error_check(" ")
        self.cur_pos += 1

        params = []
        s = ""

        while self.cur_pos < len(self.cur_line):
            if self.cur_line[self.cur_pos] == "[":
                params.append(Token("["))
                self.cur_pos += 1
            
            s = self.get_str()
            t = Token(s)

            if len(params) >= len(expected_params) or t.type != expected_params[len(params)]:
                raise ParserException(f"Invalid parameter for '{opcode}': {t}")

            params.append(t)

            if self.cur_pos >= len(self.cur_line):
                break
            
            try:
                self.error_check(",")
                self.cur_pos += 1
                self.error_check(" ")
                self.cur_pos += 1
            except ParserException as e:
                if self.cur_line[self.cur_pos] != "]":
                    raise e
                params.append(Token("]"))
                break
        
        if self.has_label:
            return Instruction(opcode, params, label=self.cur_label)
        return Instruction(opcode, params)

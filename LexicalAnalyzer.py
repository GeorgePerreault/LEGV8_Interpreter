from string import ascii_letters
from Instruction import Instruction
from Token import Token, TOKEN_TYPE_NAMES
from InstructionSet import INSTRUCTION_SET, TTS, PARAMS

ALLOWED_CHARS = {*ascii_letters, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}

class ParserError(Exception):
    pass

class LexicalAnalyzer:
    def __init__(self, file):
        self.file = open(file, "r")
        self.cur_pos = 0
        self.cur_line = ""
        self.cur_label = ""
        self.has_label = False
        self.eof = False

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
        if self.cur_line[self.cur_pos] == ":": #Not an opcode was actually a label
            self.cur_pos += 1
            
            self.set_label(opcode)

            if self.cur_pos >= len(self.cur_line):
                return None

            self.error_check(" ")

            opcode = self.get_str()

        return opcode


    def get_params(self, expected_params):
        params = []

        for expec in expected_params:
            method = self.get_one
            if expec in (TTS.REGISTER, TTS.IMMEDIATE, TTS.LABEL):
                method = self.get_str

            t = Token(method())
            if t.type != expec:
                raise ParserError(f"Expected {TOKEN_TYPE_NAMES[expec]} but got: {t} of type {TOKEN_TYPE_NAMES[t.type]}")
            params.append(t)

            if expec == TTS.COMMA:
                self.error_check(" ")

        return params

    def get_instruction(self):
        s = self.file.readline()
        if s == "":
            self.eof = True
            return None
        
        self.cur_line = " ".join(s.split()) #Removes excess spaces

        if self.cur_line == "":
            return None

        self.cur_pos = 0

        opcode = self.get_opcode()
        if not opcode:
            return Instruction(None, None, label=self.cur_label)
        self.error_check(" ")

        try:
            expected_params = INSTRUCTION_SET[opcode][PARAMS]
        except KeyError:
            raise ParserError(f"Invalid opcode: {opcode}")

        params = self.get_params(expected_params)
        
        if self.has_label:
            return Instruction(opcode, params, label=self.cur_label)
        return Instruction(opcode, params)

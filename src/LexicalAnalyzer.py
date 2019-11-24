from string import ascii_letters
from src.Instruction import Instruction
from src.Token import Token, TOKEN_TYPE_NAMES
from src.InstructionSet import INSTRUCTION_SET, TTS, PARAMS
from src.Exceptions import ParserError, TokenError, ImmediateError

ALLOWED_CHARS = {*ascii_letters, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
SINGLE_CHAR_TOKENS = {",", "[", "]", "#"}
PARAM_TOKENS = {TTS.REGISTER, TTS.IMMEDIATE, TTS.LABEL}

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

    # Raises an error if the current character isn't match
    def error_check(self, match):
        if self.cur_pos >= len(self.cur_line):
            raise ParserError(f"{self.cur_line}\nInvalid syntax. Expected: '{match}' but line was empty")
        if self.cur_line[self.cur_pos] != match:
            raise ParserError(f"{self.cur_line}\nInvalid syntax. Expected: '{match}' but got {self.cur_line[self.cur_pos]}")
        self.cur_pos += 1

    # Returns true if there's a breakpoint and also removes it from the line
    def get_breakpoint(self):
        if len(self.cur_line) > 1 and self.cur_line[-1] == "@" and self.cur_line[-2] == " ":
            self.cur_line = self.cur_line[:-2]
            return True
        return False

    # Returns the opcode (or None if these isn't one)
    def get_opcode(self):
        opcode = self.get_token()
        if opcode == "":
            raise ParserError(f"{self.cur_line}\nExpected opcode")
        if self.cur_pos < len(self.cur_line) and self.cur_line[self.cur_pos] == ":":
            # Not an opcode was actually a label
            self.cur_pos += 1
            self.set_label(opcode)

            if self.cur_pos >= len(self.cur_line):
                return None
            self.error_check(" ")
            opcode = self.get_token()

        return opcode

    # Gets params and makes sure the parameters are what we're expecting for the opcode 
    def get_params(self, expected_params):
        params = []
        
        for expec in expected_params:
            val = self.get_token()
    
            try:
                t = Token(val, expec)
            except TokenError:
                raise ParserError(f"Expected {TOKEN_TYPE_NAMES[expec]} but got: {val}")
            except ImmediateError:
                raise ParserError(f"Invalid immediate value: {val}. Must be less than 4096") 
            
            if expec in PARAM_TOKENS:
                params.append(t)

            if expec == TTS.COMMA:
                self.error_check(" ")

        # If there were more characters than expected
        if self.cur_pos < len(self.cur_line):
            raise ParserError(f"Unexpected token: {self.cur_line[self.cur_pos:]}")

        return params

    def get_token(self):
        s = ""
        while self.cur_pos < len(self.cur_line):
            c = self.cur_line[self.cur_pos]

            if c not in ALLOWED_CHARS:
                if c in SINGLE_CHAR_TOKENS and s == "":
                    self.cur_pos += 1
                    return c
                break

            s += c
            self.cur_pos += 1

        return s


    def get_instruction(self):
        # Parser is non-case sensitive
        og_line = self.file.readline().lower()
        if og_line == "":
            self.eof = True
            return None
        
        # Removes excess spaces
        self.cur_line = " ".join(og_line.split())

        # Blank line but not end of file
        if self.cur_line == "":
            return None
        
        self.cur_pos = 0
        b_point = self.get_breakpoint()

        opcode = self.get_opcode()
        if not opcode:
            return Instruction(None, None, label=self.cur_label, b_point=b_point)
        self.error_check(" ")

        try:
            expected_params = INSTRUCTION_SET[opcode][PARAMS]
        except KeyError:
            raise ParserError(f"{og_line.strip()}\nInvalid opcode: {opcode}")
        
        try:
            params = self.get_params(expected_params)
        except (ParserError, TokenError) as e:
            raise ParserError(f"{og_line.strip()}\n{e}")
    
        if self.has_label:
            return Instruction(opcode, params, label=self.cur_label, b_point=b_point)
        return Instruction(opcode, params, b_point=b_point)

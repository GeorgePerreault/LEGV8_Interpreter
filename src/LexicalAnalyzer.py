from string import ascii_letters
from src.Instruction import Instruction
from src.Token import Token, TOKEN_TYPE_NAMES
from src.InstructionSet import INSTRUCTION_SET, TTS, PARAMS
from src.Exceptions import ParserError, TokenError, ImmediateError

# ALLOWED_CHARS = {*ascii_letters, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
SINGLE_CHAR_TOKENS = {",", "[", "]", "#"}
HAULT_CHARS = {*SINGLE_CHAR_TOKENS, " ", "\t", "\n", ":"}
PARAM_TOKENS = {TTS.REGISTER, TTS.IMMEDIATE, TTS.LABEL}

class LexicalAnalyzer:
    def __init__(self, file):
        self.file = open(file, "r")
        self.cur_pos = 0
        self.cur_line = ""
        self.cur_label = None
        self.eof = False

    def get_label(self):
        if not self.cur_label:
            raise Exception("Tried to get non-existent label")
        ret = self.cur_label
        self.cur_label = None
        return ret

    def set_label(self, label):
        if self.cur_label:
            raise Exception("Overwrote existing label")
        self.cur_label = label

    def in_bounds(self):
        return self.cur_pos < len(self.cur_line)

    def cur_char(self):
        return self.cur_line[self.cur_pos]

    def remove_comments(self):
        i = self.cur_line.find("//")
        if i != -1:
            self.cur_line = self.cur_line[:i]
            return True
        return False

    # Raises an error if the current character isn't a space
    def error_check_space(self, after):
        if not self.in_bounds():
            raise ParserError(f"{self.cur_line}\nInvalid syntax. Expected more after {after}, but line was empty")
        if self.cur_char() != " ":
            raise ParserError(f"{self.cur_line}\nInvalid syntax. Expected a space after {after}, but got {self.cur_char()}")
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
            return None
        if self.in_bounds() and self.cur_char() == ":":
            # Not an opcode was actually a label
            self.cur_pos += 1
            self.set_label(opcode)

            if not self.in_bounds():
                return None
            self.error_check_space("colon")
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
                raise ParserError(f"Invalid immediate value: {val}. Must be between 0 and 4095") 
            
            params.append(t)

            if expec == TTS.COMMA:
                self.error_check_space("comma")

        # If there were more characters than expected
        if self.in_bounds():
            raise ParserError(f"Unexpected token: {self.cur_line[self.cur_pos:]}")

        return params

    def get_token(self):
        s = ""

        if self.in_bounds():
            c = self.cur_char()
            if c in SINGLE_CHAR_TOKENS:
                self.cur_pos += 1
                return c

        while self.in_bounds():
            c = self.cur_char()
            if c in HAULT_CHARS:
                break
            s += c
            self.cur_pos += 1

        return s


    def get_instruction(self):
        # Parser is non-case sensitive
        og_line = self.file.readline().lower()
        self.cur_line = og_line

        if self.cur_line == "":
            self.eof = True
            return None
        
        self.remove_comments()

        # Removes excess spaces
        self.cur_line = " ".join(self.cur_line.split())

        # Blank line but not end of file
        if self.cur_line == "":
            return None
        
        self.cur_pos = 0
        b_point = self.get_breakpoint()

        opcode = self.get_opcode()
        if not opcode:
            return Instruction(None, None, label=self.cur_label, b_point=b_point)
        self.error_check_space("opcode")

        try:
            expected_params = INSTRUCTION_SET[opcode][PARAMS]
        except KeyError:
            raise ParserError(f"{og_line.strip()}\nInvalid opcode: {opcode}")
        
        try:
            params = self.get_params(expected_params)
        except (ParserError, TokenError) as e:
            raise ParserError(f"{og_line.strip()}\n{e}")
    
        return Instruction(opcode, params, label=self.cur_label, b_point=b_point)
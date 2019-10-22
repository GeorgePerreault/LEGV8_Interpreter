from Register import ZERO_REG, LINK_REG, FRAME_POINTER, STACK_POINTER, special_reg_names

from InstructionSet import TOKEN_TYPE_NAMES, TTS

class TokenError(Exception):
    pass

class Token:
    
    def __init__(self, val: str):
        self.val = val

        val = val.lower()
        
        self.type = None
        self.r_val = None
        self.i_val = None
        self.l_val = None

        if len(val) < 1:
            raise TokenError(f"Invalid blank token generated: '{val}'")

        if val[0] == "x":
            if val[1:] == "zr":
                self.r_val = ZERO_REG
                self.type = TTS.REGISTER
                return
            try:
                self.r_val = int(val[1:])
                self.type = TTS.REGISTER
                return
            except ValueError:
                pass

        if val in ["lr", "fp", "sp"]:
            self.type = TTS.REGISTER
            if val == "lr":
                self.r_val = LINK_REG
            elif val == "fp":
                self.r_val = FRAME_POINTER
            elif val == "sp":
                self.r_val = STACK_POINTER
            return

        if val[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            try:
                self.i_val = int(val)
                self.type = TTS.IMMEDIATE
                return
            except ValueError:
                raise TokenError(f"Invalid immediate value: {val[1:]}")

        if val == "[":
            self.type = TTS.OPEN_SQUARE
            return
        if val == "]":
            self.type = TTS.CLOSE_SQUARE
            return
        if val == ",":
            self.type = TTS.COMMA
            return
        if val == "#":
            self.type = TTS.HASH
            return

        self.type = TTS.LABEL
        self.l_val = val

    def __repr__(self):
        if self.type == TTS.REGISTER:
            if self.r_val < 28:
                return f"X{self.r_val}"
            return special_reg_names(self.r_val)
        
        if self.type == TTS.IMMEDIATE:
            return f"{self.i_val}"
        if self.type == TTS.LABEL:
            return f"{self.l_val}"
        if self.type == TTS.OPEN_SQUARE:
            return "["
        if self.type == TTS.CLOSE_SQUARE:
            return "]"
        if self.type == TTS.COMMA:
            return ","
        if self.type == TTS.HASH:
            return "#"
        return NotImplemented
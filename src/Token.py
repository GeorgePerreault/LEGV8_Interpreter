from src.Register import ZERO_REG, LINK_REG, FRAME_POINTER, STACK_POINTER, special_reg_names
from src.InstructionSet import TOKEN_TYPE_NAMES, TTS
from src.Exceptions import TokenError

class Token:

    def __init__(self, val: str, expec):
        self.val = val
        self.type = None
        self.r_val = None
        self.i_val = None
        self.l_val = None
        
        if expec == TTS.REGISTER:
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
                    raise TokenError(f"Invalid register value: {val}")

            elif val in ["lr", "fp", "sp"]:
                self.type = TTS.REGISTER
                if val == "lr":
                    self.r_val = LINK_REG
                elif val == "fp":
                    self.r_val = FRAME_POINTER
                elif val == "sp":
                    self.r_val = STACK_POINTER
                return

        if expec == TTS.IMMEDIATE:
            try:
                self.i_val = int(val)
                self.type = TTS.IMMEDIATE
                return
            except ValueError:
                raise TokenError(f"Invalid immediate value: {val}")

        if expec == TTS.OPEN_SQUARE and val == "[":
            self.type = TTS.OPEN_SQUARE
            return
        elif expec == TTS.CLOSE_SQUARE and val == "]":
            self.type = TTS.CLOSE_SQUARE
            return
        elif expec == TTS.COMMA and val == ",":
            self.type = TTS.COMMA
            return
        elif expec == TTS.HASH and val == "#":
            self.type = TTS.HASH
            return

        if expec == TTS.LABEL:
            self.type = TTS.LABEL
            self.l_val = val
            return

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
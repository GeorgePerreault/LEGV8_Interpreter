from Register import ZERO_REG, LINK_REG, FRAME_POINTER, STACK_POINTER

REGISTER = 1
IMMEDIATE = 2
LABEL = 3
OPEN_SQUARE = 4
CLOSE_SQUARE = 5
REGISTER_NC = 6
IMMEDIATE_NH = 7

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
            raise ValueError(f"Token(val) had a len of {len(val)}. val = '{val}'")

        if val[0] == "x":
            if val[1:] == "zr":
                self.r_val = ZERO_REG
                self.type = REGISTER
                return
            try:
                self.r_val = int(val[1:])
                self.type = REGISTER
                return
            except ValueError:
                pass

        if val in ["lr", "fp", "sp"]:
            self.type = REGISTER
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
                self.type = IMMEDIATE
                return
            except ValueError:
                raise TokenError(f"Invalid immediate value: {val[1:]}")

        if val == "[":
            self.type = OPEN_SQUARE
            return
        if val == "]":
            self.type = CLOSE_SQUARE
            return
        
        self.type = LABEL
        self.l_val = val

    def __repr__(self):
        if self.type == REGISTER or self.type == REGISTER_NC:
            return f"X{self.r_val}"
        if self.type == IMMEDIATE:
            return f"#{self.i_val}"
        if self.type == LABEL:
            return f"{self.l_val}"
        if self.type == OPEN_SQUARE:
            return "["
        if self.type == CLOSE_SQUARE:
            return "]"
        return NotImplemented
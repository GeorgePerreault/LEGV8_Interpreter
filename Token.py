REGISTER = 1
IMMEDIATE = 2
LABEL = 3
OPEN_SQUARE = 4
CLOSE_SQUARE = 5

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
            raise ValueError(f"Token(val) had a len of {len(val)}. val = {val}")

        if val[0] == "x":
            if val[1:] == "zr":
                self.r_val = 31 #ALERT: hardcoded zero number
                self.type = REGISTER
                return
            try:
                self.r_val = int(val[1:])
                self.type = REGISTER
                return
            except ValueError:
                pass
        
        if val[0] == "#":
            try:
                self.i_val = int(val[1:])
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
        if self.type == REGISTER:
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
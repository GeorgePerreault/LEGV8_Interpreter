REGISTER = 1
IMMEDIATE = 2
MEMORY_ACCESS = 3
LABEL = 4
COMMA = 5

class TokenException(Exception):
    pass

class Token:
    
    def __init__(self, val: str):
        val = val.lower()
        
        self.type = None
        self.r_number = None
        self.i_val = None
        
        if len(val) < 1:
            raise ValueError(f"Token(val) had a len of {len(val)}. val = {val}")

        if val[0] == "x":
            try:
                self.r_number = int(val[1:])
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
                raise TokenException(f"Invalid immediate value: {val[1:]}")

        if val == ",":
            self.type = COMMA
            return

    def __repr__(self):
        return f"X{self.r_number}"
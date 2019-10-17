from Token import COMMA, REGISTER, IMMEDIATE, LABEL, OPEN_SQUARE, CLOSE_SQUARE, HASH
math_r = (REGISTER, COMMA, REGISTER, COMMA, REGISTER)
math_i = (REGISTER, COMMA, REGISTER, COMMA, HASH, IMMEDIATE)
mem = (REGISTER, COMMA, OPEN_SQUARE, REGISTER, COMMA, HASH, IMMEDIATE, CLOSE_SQUARE)

INSTRUCTION_SET = {
    "add": math_r,
    "addi": math_i,
    "adds": math_r,
    "addis": math_i,
    "ldur": mem,
    "ldurw": mem,
    "ldurh": mem,
    "ldurb": mem,
    "stur": mem,
    "sturw": mem,
    "sturh": mem,
    "sturb": mem,
    "b": (LABEL,)
}
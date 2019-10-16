from Token import REGISTER, IMMEDIATE, OPEN_SQUARE, CLOSE_SQUARE, LABEL

math_r = (REGISTER, REGISTER, REGISTER)
math_i = (REGISTER, REGISTER, IMMEDIATE)
mem = (REGISTER, OPEN_SQUARE, REGISTER, IMMEDIATE, CLOSE_SQUARE)

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
}
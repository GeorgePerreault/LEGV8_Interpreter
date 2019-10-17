class TTS:
    COMMA = 0
    REGISTER = 1
    IMMEDIATE = 2
    LABEL = 3
    OPEN_SQUARE = 4
    CLOSE_SQUARE = 5
    HASH = 6

TOKEN_TYPE_NAMES = (
    "COMMA",
    "REGISTER",
    "IMMEDIATE",
    "LABEL",
    "OPEN_SQUARE",
    "CLOSE_SQUARE",
    "HASH"
)

math_r = (TTS.REGISTER, TTS.COMMA, TTS.REGISTER, TTS.COMMA, TTS.REGISTER)
math_i = (TTS.REGISTER, TTS.COMMA, TTS.REGISTER, TTS.COMMA, TTS.HASH, TTS.IMMEDIATE)
mem = (TTS.REGISTER, TTS.COMMA, TTS.OPEN_SQUARE, TTS.REGISTER, TTS.COMMA, TTS.HASH, TTS.IMMEDIATE, TTS.CLOSE_SQUARE)

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
    "b": (TTS.LABEL,)
}
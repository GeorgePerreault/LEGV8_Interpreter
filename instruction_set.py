from Token import REGISTER, IMMEDIATE, MEMORY_ACCESS

INSTRUCTION_SET = {
    "add": ((REGISTER, REGISTER, REGISTER), lambda x,y,z: x.assign(y+z)),
    "addi": ((REGISTER, REGISTER, IMMEDIATE), lambda x,y,z: x.assign(y+z))
}
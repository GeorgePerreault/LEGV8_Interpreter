from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer

class Driver:
    
    def __init__(self, file):
        self.file = file
        self.code = [None]
        self.labels = {}

    def code_dump(self):
        for (line, inst) in enumerate(i for i in self.code if i):
            s = f"{line} "
            if inst.label:
                s += f"{inst.label}: "
            s += f"\t\t{inst}"
            print(s)

    def generate_code(self):
        lex = LexicalAnalyzer(self.file)
        line_num = 0

        while True:
            line_num += 1
            inst = lex.get_instruction()

            self.code.append(inst)

            if inst is None:
                if lex.eof:
                    break
                continue

            if lex.has_label:
                self.labels[lex.get_label()] = line_num
    
    def run(self):
        cpu = CPU()

        while cpu.pc < len(self.code):
            inst = self.code[cpu.pc]
            if not inst:
                cpu.pc += 1
                continue

            cpu.decode(inst, self.labels)
            cpu.execute()

        cpu.reg_dump(mode="dec")
        # cpu.mem_dump()
        # self.code_dump()
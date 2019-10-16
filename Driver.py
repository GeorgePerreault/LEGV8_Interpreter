from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer

class Driver:
    
    def __init__(self, file):
        self.file = file
        self.code = []
        self.labels = {}

    def code_dump(self):
        for inst in self.code:
            s = ""
            if inst.label:
                s += f"{inst.label}: "
            s += f"\t\t{inst}"
            print(s)

    def generate_code(self):
        lex = LexicalAnalyzer(self.file)
        line_num = -1

        while True:
            line_num += 1
            inst = lex.get_instruction()

            if inst is None:
                break

            self.code.append(inst)
            if lex.has_label:
                self.labels[lex.get_label()] = line_num
    
    def run(self):
        cpu = CPU()

        for inst in self.code:
            cpu.decode(inst, self.labels)
            cpu.execute()

        cpu.reg_dump()
        self.code_dump()
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

    def run(self):
        lex = LexicalAnalyzer(self.file)
        cpu = CPU()

        while True:
            try:
                inst = self.code[cpu.ip]
            except IndexError:
                inst = lex.get_instruction()

            if inst is None:
                break
            self.code.append(inst)

            if lex.has_label:
                self.labels[lex.get_label()] = cpu.ip

            cpu.decode(inst)
            cpu.execute()

        cpu.reg_dump()
        self.code_dump()
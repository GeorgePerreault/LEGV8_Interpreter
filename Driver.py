from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer

class Driver:
    
    def __init__(self, file):
        self.file = file
        self.code = []

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

            cpu.decode(inst)
            cpu.execute()

        print(cpu)
        print(self.code)
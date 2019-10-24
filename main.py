from Driver import Driver
from LexicalAnalyzer import ParserError

def main():
    d = Driver("input.leg")
    try:
        d.generate_code()
    except Exception as e:
        print(f"-----ERROR-----\n{e}")
        exit()
    d.run()

if __name__ == "__main__":
    main()
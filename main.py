from Driver import Driver
from test_all import test_bits

def main():
    d = Driver("input.leg")
    d.generate_code()
    d.run()

if __name__ == "__main__":
    main()
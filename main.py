from Driver import Driver

def main():
    d = Driver("input.leg")
    d.generate_code()
    d.run()

if __name__ == "__main__":
    main()
from Driver import Driver
from Debugger import Debugger
import sys

def main():
    file = ""
    mode = "dec"

    if len(sys.argv) < 2:
        print("No input file given")
        exit()

    file = sys.argv[1]

    if "-hex" in sys.argv:
        mode = "hex"
    elif "-bin" in sys.argv:
        mode = "bin"

    driver = Driver(file, mode=mode)
    start(file, driver)

    if "-d" in sys.argv:
        debug(driver)
    else:
        run(driver)

def start(file, driver):
    try:
        driver.generate_code()
    except Exception as e:
        print(f"-----ERROR-----\n{e}")
        exit()

def run(driver):
    driver.run()
    driver.reg_dump()

def debug(driver):
    bug = Debugger(driver)
    bug.debug()
    driver.reg_dump()

if __name__ == "__main__":
    main()
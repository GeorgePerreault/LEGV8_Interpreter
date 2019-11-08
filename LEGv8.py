from src.Driver import Driver
from src.Debugger import Debugger
from src.Arguments import Arguments
from src.Exceptions import LEGError
import sys

def main():
    args = Arguments(sys.argv)

    driver = Driver(args.file, mode=args.mode)

    try:
        driver.generate_code()
        if args.debug:
            debug(driver)
        else:
            run(driver)
    except LEGError as e:
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
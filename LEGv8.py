from src.Driver import Driver
from src.Debugger import Debugger
from src.Arguments import Arguments
import sys

def main():
    args = Arguments(sys.argv)

    driver = Driver(args.file, mode=args.mode)
    start(args.file, driver)

    if args.debug:
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
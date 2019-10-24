from Driver import Driver
from Debugger import Debugger

def main(file):
    start("input.leg")

def start(file):
    driver = Driver(file)

    try:
        driver.generate_code()
    except Exception as e:
        print(f"-----ERROR-----\n{e}")
        exit()

    run(driver)

def run(driver):
    driver.run()

def debug(driver):
    bug = Debugger(driver)
    bug.debug()

if __name__ == "__main__":
    main("input.leg")
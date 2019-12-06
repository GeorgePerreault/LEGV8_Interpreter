from src.Exceptions import DebugCommandError
from src.UsefulFuncs import get_reg_num_from_str

class DebugCommandParser:

    def __init__(self):
        # Command names are modeled after gdb
        self.ALLOWED_ACTIONS = {"continue", "next", "list", "mode", "help", "print"}
        self.ALLOWED_ACTIONS = {*self.ALLOWED_ACTIONS, *(i[0] for i in self.ALLOWED_ACTIONS)}


    def parse_command(self, s):        
        s = s.strip()
        n = s.find(" ")

        if n != -1:
            action = s[:n]
            param = s[n+1:]
        else:
            action = s
            param = None

        if action not in self.ALLOWED_ACTIONS:
            raise DebugCommandError(f"Invalid command: {action}")
        # Set the action to just be the first letter if it wasn't already
        action = action[0]

        if not param and action in {"m"}:
            raise DebugCommandError(f"This command requires a paramter")
        if param and action in {"c", "n", "h"}:
            raise DebugCommandError(f"This command does not need a paramter")

        if not param:
            return action, param

        if action == "l":
            try:
                param = int(param)
                if param < 1:
                    raise ValueError
            except ValueError:
                raise DebugCommandError(f"Invalid parameter for command list: {param}")

        elif action == "m":
            if param not in ("dec", "udec", "hex", "bin"):
                raise DebugCommandError(f"Invalid parameter for command mode: {param}")

        elif action == "p":
            if param:
                reg = get_reg_num_from_str(param)
                if reg is None:
                    raise DebugCommandError(f"Invalid register value for command print: {param}")
                param = reg
            else:
                raise DebugCommandError(f"Invalid parameter for command print: {param}")

        return action, param
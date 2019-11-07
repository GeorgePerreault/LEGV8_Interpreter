class DebugCommandError(Exception):
    pass

class DebugCommandParser:

    def __init__(self):
        # Modeled after gdb
        self.ALLOWED_ACTIONS = ("continue", "step", "list", "mode", "c", "s", "l", "m")


    def parse_command(self, s):        
        s = s.split()

        action = s[0]
        param = s[1] if len(s) == 2 else None
        mode = None
        spread = None

        if action not in self.ALLOWED_ACTIONS:
            raise DebugCommandError(f"Invalid command: {action}")
        # Set the  action just be the first letter if it wasn't already
        action = action[0]

        if not param:
            return action, mode, spread

        if action[0] == "l":
            try:
                spread = int(param)
                if spread < 1:
                    raise ValueError
            except ValueError:
                raise DebugCommandError(f"Invalid parameter for command list: {param}")

        elif action[0] == "m":
            if param not in ("dec", "udec", "hex", "bin"):
                raise DebugCommandError(f"Invalid parameter for command mode: {param}")
            mode = param

        return action, mode, spread
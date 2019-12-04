from src.Exceptions import DebugCommandError

class DebugCommandParser:

    def __init__(self):
        # Modeled after gdb
        self.ALLOWED_ACTIONS = {"continue", "next", "list", "mode", "help", "print"}
        self.ALLOWED_ACTIONS = {*self.ALLOWED_ACTIONS, *(i[0] for i in self.ALLOWED_ACTIONS)}


    def parse_command(self, s):        
        s = s.split()

        action = s[0]
        param = s[1] if len(s) == 2 else None

        if action not in self.ALLOWED_ACTIONS:
            raise DebugCommandError(f"Invalid command: {action}")
        # Set the action to just be the first letter if it wasn't already
        action = action[0]

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
            if param[0].lower() == "x" and len(param) > 1:
                reg = param[1:]
                try:
                    param = int(reg)
                except ValueError:
                    raise DebugCommandError(f"Invalid register value for command print: {param}")
            else:
                raise DebugCommandError(f"Invalid parameter for command print: {param}")

        return action, param
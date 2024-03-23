#!/usr/bin/python3
"""The Consol Module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB class"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit The Console"""
        return True

    def do_EOF(self, line):
        """Quit The Console"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""The Consol Module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB class"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """Quit The Console"""
        return True

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
Command interpreter for the AirBnB project
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
This module defines the HBNBCommand class,
a command interpreter for the Airbnb clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Implementation of a command interpreter for the Airbnb clone project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using Ctrl-D (EOF)
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Empty line handler (does nothing)
        """
        pass

    def help_quit(self):
        """
        Display help message for quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help message for EOF command (Ctrl-D to exit)
        """
        print("Exit the program using Ctrl-D (EOF)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

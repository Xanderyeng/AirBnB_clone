#!/usr/bin/python3
"""
This module defines the HBNBCommand class,
a command interpreter for the Airbnb clone project.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    command interpreter for the Airbnb clone project.
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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name in BaseModel.__subclasses__():
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all <class_name> or all
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            if arg in BaseModel.__subclasses__():
                print(
                        [str(obj) for key,
                            obj in storage.all().items()
                            if arg in key]
                    )
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        all_objs = storage.all()
        if key in all_objs:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3].strip('"')
            obj = all_objs[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

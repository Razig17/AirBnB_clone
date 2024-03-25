#!/usr/bin/python3
"""The Consol Module"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB class"""

    prompt = "(hbnb)"
    classes = {"BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """Quit The Console"""
        return True

    def emptyline(self):
        """Dose not execute anything"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:

            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")

        else:
            args = shlex.split(line)
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()

                key = "{}.{}".format(args[0], args[1])
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = shlex.split(line)
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()

        commands = shlex.split(line)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif line in self.classes:
            for obj in objects.values():
                if obj.__class__.__name__ == line:
                    print(str(obj))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """

        if not line:
            print("** class name missing **")
        else:
            args = shlex.split(line)
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key not in objects.keys():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    try:
                        setattr(objects[key], args[2], eval(args[3]))
                    except NameError:
                        setattr(objects[key], args[2], args[3])
                    objects[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

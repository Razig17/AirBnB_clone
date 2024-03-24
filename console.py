#!/usr/bin/python3
"""The Consol Module"""

import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB class"""

    prompt = "(hbnb)"
    file_path = "file.json"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """Quit The Console"""
        return True

    def do_creat(self, line):
        """Creat an instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_destroy(self, line):
        """Destroy an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        with open(self.file_path, 'r') as file:
            all_data = json.load(file)
            key = class_name + '.' + instance_id
            if key in all_data:
                del all_data[key]
                with open(self.file_path, 'w') as file:
                    json.dump(all_data, file)
            else:
                print("** no instance found **")
            
    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        if args[1] != args[0].id:
            print("** no instance found **")
            return
        class_name = args[0]
        instance_id = args[1]
        with open(self.file_path, 'r') as file:
            all_data = json.load(file)
            key = class_name + '.' + instance_id
            print(all_data[key])

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

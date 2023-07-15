#!/usr/bin/python3

import cmd
import json
import models
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()  # New line after EOF
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in models.storage.all():
                print(models.storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in models.storage.all():
                del models.storage.all()[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of instances"""
        args = split(arg)
        if args and args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            instances = []
            if args[0] in models.classes:
                instances = models.classes[args[0]].all()
            else:
                for obj in models.storage.all().values():
                    if not args or obj.__class__.__name__ == args[0]:
                        instances.append(str(obj))
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in models.storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = models.storage.all()[obj_key]
                if obj.__class__.__name__ not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                    args[3] = args[3][1:-1].replace('"', '')
                setattr(obj, args[2], self.cast_value(args[3]))
                obj.save()

    def cast_value(self, value):
        """Cast the value to int or float if possible"""
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

if __name__ == '__main__':
    HBNBCommand().cmdloop()

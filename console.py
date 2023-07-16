#!/usr/bin/python3
"""
Contains the HBNBCommand class
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D)
        """
        print()  # New line after EOF
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[obj_key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(obj_key)
                storage.save()

    def do_all(self, arg):
        """
        Print all string representations of all instances
        """
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            for obj_key in storage.all():
                obj_list.append(str(storage.all()[obj_key]))
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            for obj_key in storage.all():
                if obj_key.split(".")[0] == args[0]:
                    obj_list.append(str(storage.all()[obj_key]))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[obj_key]
            setattr(obj, args[2], self.cast_value(args[3]))
            storage.save()

    def cast_value(self, value):
        """
        Cast the value to int or float if possible
        """
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized
        """
        args = line.split(".")
        if len(args) >= 2:
            if args[0] in storage.classes.keys():
                command = args[1].split("(")[0]
                if command == "all":
                    self.do_all(args[0])
                elif command == "count":
                    count = 0
                    for key in storage.all():
                        if key.split(".")[0] == args[0]:
                            count += 1
                    print(count)
                elif command == "show":
                    if len(args[1].split("(")) >= 2:
                        obj_id = args[1].split("(")[1].split(")")[0]
                        line = args[0] + " " + obj_id
                        self.do_show(line)
                elif command == "destroy":
                    if len(args[1].split("(")) >= 2:
                        obj_id = args[1].split("(")[1].split(")")[0]
                        line = args[0] + " " + obj_id
                        self.do_destroy(line)
                elif command == "update":
                    if len(args[1].split("(")) >= 2:
                        obj_id = args[1].split("(")[1].split(")")[0]
                        rest = args[1].split(")")[1].strip()
                        line = args[0] + " " + obj_id + " " + rest[1:-1]
                        self.do_update(line)
        else:
            cmd.Cmd.default(self, line)

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class
        """
        args = arg.split()
        count = 0
        if len(args) == 0:
            for key in storage.all():
                count += 1
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        else:
            for key in storage.all():
                if key.split(".")[0] == args[0]:
                    count += 1
        print(count)

    def __class_command(self, args):
        """Helper method for class command"""
        if args == "all":
            self.do_all("")
        elif args == "count":
            self.do_count("")
        elif args == "show":
            print("** instance id missing **")
        elif args == "destroy":
            print("** instance id missing **")
        elif args == "update":
            print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_BaseModel(self, args):
        """
        Handle BaseModel commands
        """
        self.__class_command(args)

    def do_User(self, args):
        """
        Handle User commands
        """
        self.__class_command(args)

    def do_State(self, args):
        """
        Handle State commands
        """
        self.__class_command(args)

    def do_City(self, args):
        """
        Handle City commands
        """
        self.__class_command(args)

    def do_Amenity(self, args):
        """
        Handle Amenity commands
        """
        self.__class_command(args)

    def do_Place(self, args):
        """
        Handle Place commands
        """
        self.__class_command(args)

    def do_Review(self, args):
        """
        Handle Review commands
        """
        self.__class_command(args)

    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized
        """
        args = line.split(".")
        if len(args) >= 2:
            if args[0] in storage.classes.keys():
                command = args[1].split("(")[0]
                if command == "count":
                    self.do_count(args[0])
                elif command == "show":
                    if len(args[1].split("(")) >= 2:
                        obj_id = args[1].split("(")[1].split(")")[0]
                        line = args[0] + " " + obj_id
                        self.do_show(line)
                elif command == "destroy":
                    if len(args[1].split("(")) >= 2:
                        obj_id = args[1].split("(")[1].split(")")[0]
                        line = args[0] + " " + obj_id
                        self.do_destroy(line)
                elif command == "update":
                    if len(args[1].split("(")) >= 2:
                        obj_id = args[1].split("(")[1].split(")")[0]
                        rest = args[1].split(")")[1].strip()
                        line = args[0] + " " + obj_id + " " + rest[1:-1]
                        self.do_update(line)
        else:
            cmd.Cmd.default(self, line)

    def count(self, cls):
        """
        Retrieve the number of instances of a class
        """
        count = 0
        for key in storage.all():
            if key.split(".")[0] == cls.__name__:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()


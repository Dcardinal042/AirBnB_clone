#!/usr/bin/python3
<<<<<<< HEAD
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from re import search


class HBNBCommand(cmd.Cmd):
    """
        Summary: class that define the command interpreter:
    """
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "Place", "State", "City",
                    "Amenity", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    def do_EOF(self, line):
        "Exit the program with Ctrl+D"
        return True

    def do_quit(slef, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything
            If the line is empty, emptyline() is called,
            the method was modified because the default
            implementation runs the previous command again
            and we want it to pass not executing anything.
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        args_list = arg.split(" ")
        if not args_list[0]:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.list_classes:
            new_instance = globals()[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """deletes an instance for the dictionary
                """
                storage.all().pop(id_object)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not
            on the class name
        """
        element_list = []
        args_list = arg.split()
        if len(args_list) == 0:
            for key, value in storage.all().items():
                element_list.append(str(value))
            print(element_list)
        elif args_list[0] in HBNBCommand.list_classes:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args_list[0]:
                    element_list.append(str(value))
            print(element_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
           updating attribute  (save the change into the JSON file).
        """
        args_list = shlex.split(arg[:])
        arg = arg.split(" ")
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            "if the instance of the class name doesn’t exist for the id"
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                dog = r"\d+\.\d+"
                id_object = "{}.{}".format(args_list[0], args_list[1])
                name_attr = args_list[2]
                value = args_list[3]
                """ Only “simple” arguments can be updated: string,
                    integer and float. """
                if '"' in arg[3]:
                    pass
                elif search(dog, arg[3]):
                    value = float(value)
                elif arg[3].isdigit():
                    value = int(value)
                setattr(storage.all()[id_object], name_attr, value)
                storage.all()[id_object].save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        count = 0
        for key, value in storage.all().items():
            if key.split(".")[0] == arg:
                count += 1
        print(count)

    def default(self, arg):
        """Method called on an input line when the command prefix is
        not recognized. If this method is not overridden, it prints an
        error message and returns. """
        # BaseModel show("440f0fd5-502f-4f46-bc09-6b2c1b156fa7")
        args_list = arg.split(".", 1)
        if args_list[0] in HBNBCommand.list_classes:  # BaseModel
            method = args_list[1].split("(")  # show
            # retrieve all instances of a class by using: <class name>.all()
            if method[0] == "all":
                return self.do_all(args_list[0])
            # retrieve the number of instances of a class: <class name>.count()
            elif method[0] == "count":
                return self.do_count(args_list[0])
            elif method[0] == "show":
                id_show = args_list[1].split('"')
                args_show = "{} {}".format(args_list[0], id_show[1])
                return self.do_show(args_show)
            elif method[0] == "destroy":
                id_destroy = args_list[1].split('"')
                args_destroy = "{} {}".format(args_list[0], id_destroy[1])
                return self.do_destroy(args_destroy)
            elif method[0] == "update":
                part1 = method[1].replace(")", "")
                check_dict = part1[:].split(", ")
                if check_dict[1][0] is "{":
                    class_id = check_dict[0].replace('"', "")
                    dog = r"\d+\.\d+"
                    for i in range(1, len(check_dict)):
                        dict_parse = check_dict[i].replace("{", "", 1)
                        dict_parse = dict_parse.replace("}", "")
                        dict_parse = dict_parse.replace("'", "")
                        dict_parse = dict_parse.split(": ")
                        if '"' in dict_parse[1]:
                            pass
                        elif search(dog, dict_parse[1]):
                            dict_parse[1] = float(dict_parse[1])
                        elif dict_parse[1].isdigit():
                            dict_parse[1] = int(dict_parse[1])
                        args_update = "{} {} {} {}".format(args_list[0],
                                                           class_id,
                                                           dict_parse[0],
                                                           dict_parse[1])
                        self.do_update(args_update)
                else:
                    part2 = part1.replace('"', "", 4)
                    part3 = part2.split(", ")
                    args_update = "{} {} {} {}".format(args_list[0], part3[0],
                                                       part3[1], part3[2])
                    return self.do_update(args_update)


if __name__ == "__main__":
=======
""" console """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
>>>>>>> bcefee43995a33a597f14dd24c126f9585732e2a
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Airbnb console command interpreter.

    This class provides a command-line interface for interacting with Airbnb-like
    objects. It supports commands for creating, showing, destroying, listing, updating,
    and quitting the application.

    Attributes:
    - prompt (str): The command prompt displayed to the user.
    - classess (dict): A dictionary mapping class names to their corresponding classes.

    Methods:
    - do_create(self, line): Creates a new instance of a specified class, saves it, and prints the ID.
    - do_show(self, line): Prints the string representation of an instance based on class name and ID.
    - do_destroy(self, line): Deletes an instance based on class name and ID.
    - do_all(self, line): Prints all string representations of instances or those of a specified class.
    - do_update(self, line): Updates an instance based on class name and ID with new attribute values.
    - do_quit(self, line): Exits the command interpreter.
    - do_EOF(self, line): Exits the command interpreter when encountering the end of file (EOF).
    - emptyline(self): Does nothing on an empty input line.

    Usage:
    - Run the script to start the command-line interface.
    - Enter commands such as 'create', 'show', 'destroy', 'all', 'update', 'quit', or 'EOF'.
    - Follow the prompts and instructions provided by the interpreter.

    Example:
    ```
    $ ./console.py
    (hbnb) create BaseModel
    ** class name missing **
    (hbnb) show BaseModel 12345-6789
    ** instance id missing **
    (hbnb) quit
    ```
    """

    prompt = "(hbnb) "
    classess = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_create(self, line):
        """
        Create a new instance of a specified class, save it, and print the ID.

        Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classess:
            print("** class doesn't exist **")
        else:
            new_instance = self.classess[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Print the string representation of an instance based on class name and ID.

        Usage: show <class_name> <instance_id>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classess:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            print(objects.get(key, "** no instance found **"))

    def do_destroy(self, line):
        """
        Delete an instance based on class name and ID.

        Usage: destroy <class_name> <instance_id>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classess:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representations of instances or those of a specified class.

        Usage:
        - all: Print all instances.
        - all <class_name>: Print instances of a specific class.
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            for v in objects:
                strline = str(objects[v])
                print(strline)
        elif args[0] not in self.classess:
            print('** class doesn\'t exist **')
            return False
        else:
            for v in objects:
                if v.startswith(args[0]):
                    strline = str(objects[v])
                    print(strline)

    def do_update(self, line):
        """
        Update an instance based on class name and ID with new attribute values.

        Usage: update <class_name> <instance_id> <attribute_name> <attribute_value>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classess:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                setattr(objects[key], args[2], args[3])
                objects[key].save()
            else:
                print("** no instance found **")

    def do_quit(self, line):
        """
        Exit the command interpreter.

        Usage: quit
        """
        return True

    def do_EOF(self, line):
        """
        Exit the command interpreter when encountering the end of file (EOF).

        Usage: EOF
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty input line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


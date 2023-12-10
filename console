#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "
    myclasses = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.myclasses:
            print("** class doesn't exist **")
        else:
            new_instance = self.myclasses[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.myclasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            print(all_objs.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.myclasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = arg.split()
        all_objs = storage.all()

        if len(args) == 0:
            for i in all_objs:
                strarg = str(all_objs[i])
                print(strarg)
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        else:
            for i in all_objs:
                if i.startswith(args[0]):
                    strarg = str(all_objs[i])
                    print(strarg)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.myclasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            if key in all_objs:
                setattr(all_objs[key], args[2], args[3])
                all_objs[key].save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


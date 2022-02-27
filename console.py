#!/usr/bin/python3
"""
console 0.0.1
"""


from ast import Return
import cmd
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity
}
class_list = []
for key in classes:
    class_list.append(key)
commands = [
    "do_create",
    "do_show",
    "do_destroy",
    "do_all",
    "do_update",
]


class HBNBCommand(cmd.Cmd):
    """Handles prompt, EOF, quit and help arguments"""
    print("------------------------------")
    print("|    Welcome to Hbnb Console  |")
    print("|    Type help for commands   |")
    print("|    Created for Alx          |")
    print("------------------------------")
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        """Handles empty spaces when you press ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                new_instance = classes[args]()
                print(new_instance.id)
                new_instance.save()

    def do_show(self, args):
        """Prints string representation of an instance"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()

    def do_all(self, args):
        """Prints string representation of all instances"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                print(storage.all())

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                setattr(storage.all()[key],
                                        args[2], args[3])
                                storage.save()

    def get_objects(self, instance=''):
        """Gets the elements created by the console
        This method takes care of obtaining the information
        of all the instances created in the file `objects.json`
        that is used as the storage engine.
               """
        objects = models.storage.all()
        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]
        return [str(val) for key, val in objects.items()]

    def default(self, args):
        '''

        '''
        if '.' in args:
            splitted = re.split('[.(),]', args)
            class_name = splitted[0]
            method_name = splitted[1]
            if class_name in class_list:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)
                elif method_name == 'update':
                    class_id = splitted[2][1:-1]
                    print(splitted)
                    self.do_update(class_name + ' ' + class_id + ' ' + splitted[3] + ' ' + splitted[4])



if __name__ == '__main__':
    HBNBCommand().cmdloop()

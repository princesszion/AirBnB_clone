#!/usr/bin/python3
"""
Module console
Entry point for command interpreter
"""


import cmd
from models.base_model import BaseModel
from models import storage

classes = {
    "BaseModel": BaseModel
}
class_list = []
for key in classes:
    class_list.append(key)


class HBNBCommand(cmd.Cmd):
    """
    Handles prompt, EOF, quit and help arguments
    """
    print("------------------------------")
    print("|    Welcome to Hbnb Console  |")
    print("|    Type help for commands   |")
    print("|    Created for Alx          |")
    print("------------------------------")
    prompt = '(hbnb)'

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Quiting")
        return True
    
    def do_EOF(self, args):
        """Exits the console"""
        return True
    
    def emptyline(self):
        """Handles Empty argument"""
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
                new_instance.save()
                print(new_instance.id)

    
    def do_show(self, args):
        """prints the string representation of an instance"""
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id is missing **")
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
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id is missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
    
    def do_all(self, args):
        """Prints all string representation of all instances"""
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                print(storage.all())
    
    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id is missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** instance id missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                setattr(storage.all()[key]),
                                args[2], args[4]
                                storage.save()

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()

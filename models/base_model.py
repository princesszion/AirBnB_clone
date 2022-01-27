#!/usr/bin/python3
"""
Module base_models
Defines class BaseModel that defines all common attributes/methods for other classes
"""


import uuid
from datetime import datetime

class BaseModel:
    """
    defines all common attributes/methods

    Attributes:
        id
        created_at
        updated_at

        __str__(self)
        save(self)
        to_dict(self)  
    """
    def __init__(self, *args, **kwargs):
        """Initializes model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for i in kwargs:
                if i in ['created_at', 'updated_at']:
                    setattr(self, i, datetime.fromisoformat(kwargs[i]))
                elif i != '__class__':
                    setattr(self, i, kwargs[i])
                elif not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                elif not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                elif not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())
    
    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
        self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for i in dict:
            if type(dict[i]) is datetime:
                dict[i] = dict[i].isoformat()
        if 'instance' in dict.keys():
            del(dict['instance'])
        return dict

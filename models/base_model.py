"""
base_model class
"""

import models
from datetime import datetime
import uuid


class BaseModel():
    """
    BaseModel class implementation
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *arg, **kwargs):
        """
        initializes an instance
        """
        if len(kwargs)!=0:
            for key,value in kwargs.items():
                if key=="__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                      self.updated_at = datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value) 
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        prints info about an instance
        """
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) <{}>".format(a, b, c)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        

    def to_dict(self):
        """
        returns a dictionary
        containing all keys/values of __dict__ of the required instance
        """
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        print("\n-!-\n")
        print(self.created_at)
        print(type(self.created_at))
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
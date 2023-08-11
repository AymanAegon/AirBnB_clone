"""
FileStorage Model
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serealizes __objects to JSON file (path: __file_path)."""
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes the JSON file  (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key in obj_dict.items():
                    print(key)
                    class_name = key[1]["__class__"]
                    del key[1]["__class__"]
                    self.new(eval(class_name)(**key[1]))
        except FileNotFoundError:
            return
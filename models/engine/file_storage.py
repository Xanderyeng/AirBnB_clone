import json
# import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        print("Saving to json file...")
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def get(self, cls, id):
        """Retrieve an object based on class name and ID."""
        key = "{}.{}".format(cls.__name__, id)
        return self.__objects.get(key, None)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        print("Reading from json file...")
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    cls = globals()[class_name]
                    instance = cls(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass


# Creating a unique FileStorage instance
# storage = FileStorage()
# storage.reload()

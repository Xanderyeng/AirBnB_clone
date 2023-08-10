import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = os.path.join(os.path.dirname(__file__), "file.json")
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        print("Saving to json file...")
        serialized_objs = {
                key: obj.to_dict() for key, obj in self.__objects.items()
                }
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        print("Reading from json file...")
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = (
                            BaseModel if class_name == "BaseModel" else None
                            )
                    if class_obj:
                        self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass

#!/usr/bin/python3
import uuid
from datetime import datetime
import json
# from models import storage


class BaseModel:

    """Base class for all other models."""

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs_copy = kwargs.copy()
            if "__class__" in kwargs_copy:
                del kwargs_copy["__class__"]
            kwargs_copy["created_at"] = datetime.strptime(
                    kwargs_copy["created_at"], '%Y-%m-%dT%H:%M:%S.%f'
                    )
            kwargs_copy["updated_at"] = datetime.strptime(
                    kwargs_copy["updated_at"], '%Y-%m-%dT%H:%M:%S.%f'
                    )
            for key, value in kwargs_copy.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """String representation of the model."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        """self.updated_at = datetime.now().strftime("%A %d %B %Y at %H:%M:%S")"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        dict_ = {
                key: value
                for key, value in self.__dict__.items()
                if value is not None
            }
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_

    def save_to_file(self):
        """Saves the model instance to a file in JSON format."""
        filename = f"{self.__class__.__name__}_{self.id}.json"
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file)

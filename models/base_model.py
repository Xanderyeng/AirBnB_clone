#!/usr/bin/python3
import uuid
from datetime import datetime
import json
# from models import storage


class BaseModel:

    """Base class for all other models."""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'updated_at' in kwargs.keys():
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()
            if 'created_at' in kwargs.keys():
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            kwargs.pop('__class__', None)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """String representation of the model."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        from models import storage
        """self.updated_at = datetime.now().
        strftime("%A %d %B %Y at %H:%M:%S")"""
        self.updated_at = datetime.now()
        storage.new(self)
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

import uuid
from datetime import datetime


class BaseModel:

    """Base class for all other models."""

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """String representation of the model."""
    return (if "[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

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

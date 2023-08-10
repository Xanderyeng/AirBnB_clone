# models/__init__.py
# I MAY NEED THESE ONLY IF I FIND A NEED
# TO CREATE A BASEMODE FOR THEM ( INHERITANCE )


# from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# base_model_instance = BaseModel()

storage = FileStorage()
storage.reload()
# from .user import User
# from .state import State
# Add more imports for other model classes

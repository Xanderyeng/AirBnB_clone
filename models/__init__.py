#!/usr/bin/python3

# I MAY NEED THESE ONLY IF I FIND A NEED
# TO CREATE A BASEMODEL FOR THEM ( INHERITANCE )


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

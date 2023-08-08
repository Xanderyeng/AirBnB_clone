import uuid
from datetime import datetime

class BaseModel:
    """Base class for all other models."""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __init__(self, created_at, updated_at):
        self.id = 

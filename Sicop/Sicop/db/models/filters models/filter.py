import uuid
from typing import Optional
from pydantic import BaseModel, Filter

class Filter(BaseModel):
    filterBy:str
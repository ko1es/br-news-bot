from datetime import datetime
from typing import Union

from pydantic import BaseModel


class Post(BaseModel):
    url: str
    identifier: Union[str, int]
    title: str
    date: datetime
    source: str

from typing import List

from pydantic import BaseModel


class RecognitionListResponse(BaseModel):
    items: List[int]

from pydantic import BaseModel
from typing import Optional



class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100 ## 1MB in bytes
    overlap_size: Optional[int] = 20 ## 20% of chunk size
    do_reset: Optional[int] = 0 ## 0 or 1, default is 0 (false)
from typing_extensions import Protocol
from typing import Dict
import pydantic

class IWork(Protocol):

    def get_request_key(self):
        ...
    
    def get_file_name(self):
        ...

class Work(pydantic.BaseModel):
    work : Dict

    def get_request_key(self)->Dict:
        return self.work
    
    def get_file_name(self)->str:
        key_part = '_'.join(s for s in list(self.work.keys()))
        value_part = '_'.join(s for s in list(self.work.values()))
        return f'{key_part}_{value_part}'
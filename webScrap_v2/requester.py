from typing import Dict
from typing_extensions import Protocol

class IRequester(Protocol):

    def request(self, key:Dict):
        ...
from webScrap_v2.work import IWork
from typing import List
from typing_extensions import Protocol

class IWorkingList(Protocol):

    def get_working_list(self)->List[IWork]:
        ...
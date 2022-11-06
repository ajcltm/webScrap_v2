from typing import List
from typing_extensions import Protocol
import os
from webScrap_v2.work import IWork

class IWorkingListFilter(Protocol):

    # def filt_working_list(self, workedList:List, workingList:List[IWork]) -> List[IWork] :
        # ...
    def filt_working_list() :
        ...


class WorkingListFilter:

    def filt_working_list(self, workedList:List, workingList:List[IWork]) -> List[IWork]:
        if not workedList:
            return workingList
        suffix = os.path.splitext(workedList[0])[-1]
        notYetWorkedList = [i for i in workingList if not f'{i.get_file_name()}{suffix}' in workedList]                
        return notYetWorkedList
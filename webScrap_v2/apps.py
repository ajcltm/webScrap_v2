from webScrap_v2.workingList import IWorkingList
from webScrap_v2.workedList import IWorkedList, WorkedList
from webScrap_v2.workingListFilter import IWorkingListFilter, WorkingListFilter
from webScrap_v2.requester import IRequester
from webScrap_v2.fileSaver import IFileSaver, FSaver
from tqdm import tqdm
from pathlib import Path


class SScraper:

    def __init__(self, IWorkingList:IWorkingList, IWorkedList:IWorkedList, IWorkingListFilter:IWorkingListFilter, IRequester:IRequester, IFileSaver:IFileSaver, save_extention:str) -> None:
        self.wkngl = IWorkingList
        self.wkedl = IWorkedList
        self.wlf = IWorkingListFilter
        self.r = IRequester
        self.fs = IFileSaver
        self.save_extention = save_extention

    def execute(self):
        working_list = self.wkngl.get_working_list()
        worked_list = self.wkedl.get_worked_list()
        notYetWorkedList = self.wlf.filt_working_list(workedList=worked_list, workingList=working_list)
    
        for iwork in tqdm(notYetWorkedList):
            try:
                data = self.r.request(iwork.get_request_key())
            except :
                data = None
                print(f'fail to get data : {iwork}')
            if data:
                self.fs.save_file(data, iwork.get_file_name(), self.save_extention)

class FSScraper:

    def __init__(self, IWorkingList:IWorkingList, IRequester:IRequester, save_path:Path, save_extention='pickle') -> None:
        self.wkngl = IWorkingList
        self.wkedl = WorkedList(save_path)
        self.wlf = WorkingListFilter()
        self.r = IRequester
        if save_extention == 'pickle':
            saver = FSaver().get_saver(save_extention='pickle')
        saver = FSaver().get_saver(save_extention=save_extention)
        self.fs = saver(save_path)
        self.save_extention = save_extention

    def get_sscraper(self):
        return SScraper(IWorkingList=self.wkngl, IWorkedList=self.wkedl, IWorkingListFilter=self.wlf, IRequester=self.r, IFileSaver=self.fs, save_extention=self.save_extention)
        
    def execute(self):
        sscraper = self.get_sscraper()
        sscraper.execute()

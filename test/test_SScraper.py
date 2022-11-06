import unittest
from unittest.mock import Mock
from pathlib import Path
from webScrap_v2 import work, workingListFilter, fileSaver, apps

import os

class TestSScraper(unittest.TestCase):

    def tearDown(self) -> None:
        file_path = Path.cwd().joinpath('test', 'key_2345.pickle')
        os.remove(file_path)
        
    def test_valid_sscraper(self):
        work_data = [{'key': '1234'}, {'key': '2345'}]

        wkngl = Mock()
        wkngl.get_working_list.return_value = [work.Work(work=i) for i in work_data]
        
        wkedl = Mock()
        wkedl.get_worked_list.return_value = [f'{work.Work(work=work_data[0]).get_file_name()}.pickle']

        request = Mock()
        request.request.return_value = {'data_key' : 'data_value'}

        file_path = Path.cwd().joinpath('test')
        fs = fileSaver.JsonSaver(file_path)

        ss = apps.SScraper(IWorkingList=wkngl, IWorkedList=wkedl, IWorkingListFilter=workingListFilter.WorkingListFilter(), IRequester=request, IFileSaver=fs, save_extention='pickle')
        ss.execute()

class TestFSScraper(unittest.TestCase):

    def tearDown(self) -> None:
        file_path = Path.cwd().joinpath('test', 'key_2345.pickle')
        os.remove(file_path)
    
    def test_valid_fsscraper(self):
        work_data = [{'key': '1234'}, {'key': '2345'}]

        wkngl = Mock()
        wkngl.get_working_list.return_value = [work.Work(work=i) for i in work_data]
        
        request = Mock()
        request.request.return_value = {'data_key' : 'data_value'}

        save_path = Path.cwd().joinpath('test')

        ss = apps.FSScraper(IWorkingList=wkngl, IRequester=request, save_path=save_path, save_extention='pickle')
        ss.execute()

if __name__ == '__main__':
    unittest.main()


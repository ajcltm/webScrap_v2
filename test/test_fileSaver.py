import unittest
from pathlib import Path
from webScrap_v2 import work, fileSaver
import pickle
import os

class TestFileSaver(unittest.TestCase):

    def tearDown(self) -> None:
        os.remove(self.saved_file_path)

    def test_valid_data_saver(self):
        work_data = {'complexNo':"20220709", 'ptp':'a_type'}
        data = {'complexNo':"20220709", 'ptp':'a_type', 'price': 50000}
        w = work.Work(work=work_data)
        file_path = Path.cwd()
        fs = fileSaver.PickleSaver(filePath=file_path)
        fs.save_file(data, w.get_file_name())
        self.saved_file_path = f'{file_path.joinpath(w.get_file_name())}.pickle'
        with open(self.saved_file_path, mode='rb') as fr:
            load_data = pickle.load(fr)

        self.assertEqual(data, load_data)

if __name__ == '__main__':
    unittest.main()
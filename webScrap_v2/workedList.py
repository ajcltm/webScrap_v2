from typing_extensions import Protocol
from pathlib import Path
import os


class IWorkedList(Protocol):

    def get_worked_list():
        ...

class WorkedList:

    def __init__(self, workedFilePath:Path):
        self.workedFilePath = workedFilePath

    def get_worked_list(self):
        return os.listdir(self.workedFilePath)
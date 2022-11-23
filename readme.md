#### **Pickle**
---
- working list
~~~python
from webScrap_v2 import work
import datetime


class WorkingList:

    def get_day_list(self, start, end=None):
        start = datetime.datetime.strptime(start, "%Y%m%d")
        if end:
            end = datetime.datetime.strptime(end, "%Y%m%d")
        else:
            end = datetime.datetime.today()
        day_list = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]
        dayList = []
        for date in day_list:
            dayList.append(date.strftime("%Y%m%d"))
        return dayList

    def get_working_list(self):
        dayList = self.get_day_list(start = '20220101')
        return [work.Work(work={'trdDd':day}) for day in dayList]
~~~

- request
~~~python
from typing import Dict
import requests

class Request_price:

    def request(self, work:Dict):
        trdDd = work.get('trdDd')

        URL = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT01501',
            'locale': 'ko_KR',
            'mktId': 'ALL',
            'trdDd': trdDd,
            'share': '1',
            'money': '1',
            'csvxls_isNo': 'false',
        }

        r = requests.post(url=URL, data=data)

        return r.json()
~~~

- application
~~~python
from pathlib import Path
from krx_v2.webScrap import request, workingList # from 다른 폴더(모듈) import 다른 파일

from pathlib import Path
from webScrap_v2 import apps


class Scraper:

    def execute(self):
        wl = workingList.WorkingList()
        rq = request.Request_price()
        dir_ = Path.home().joinpath('Desktop', 'krx')
        s = apps.FSScraper(IWorkingList=wl, IRequester=rq, save_path=dir_)
        s.execute()
~~~
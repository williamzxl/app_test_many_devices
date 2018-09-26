import os
import yaml
import multiprocessing
from testcase.page.tests.all_task.all_task_funcs import *
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface
from testcase.interface.study_center.get_study_center_serverID import GetTaskGroupNum


class HomeWork(AllInterface):
    pass


class HomeWork1(StudyCenter, AllPage, GetTaskGroupNum):
    pass


def main_all(appium_url, d, h):
    while True:
        try:
            main1(appium_url, d, h)
        except:
            pass
        finally:
            pass


if __name__ == '__main__':
    devices = []
    with open(os.getcwd().split("testcase")[0] + "\config\devices_cfg.yml") as f:
        data = list(yaml.safe_load_all(f))
        for d in data:
            for d1 in d:
                for v in (d1.items()):
                    devices.append(v[1])
    pool = multiprocessing.Pool(processes=2)
    for device in devices:
        pool.apply_async(main_all, (device.get('appium_url'), device.get('desired_caps'), device.get("headers")))
    pool.close()
    pool.join()


























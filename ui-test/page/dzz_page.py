from common.page_common import PageCommon
from locator.dzz_locator import DzzLocator
from data.dzz_data import DzzData
import time


# 党组织管理
class DzzPage(PageCommon):
    # 点击党组织管理菜单栏
    def click_dzz(self):
        self.click_element(DzzLocator.org_menu)
        time.sleep(2)
        self.click_element(DzzLocator.dzz_menu)
        time.sleep(2)

    # 搜索党组织
    def search_dzz(self):
        self.input(DzzLocator.dzz_search, DzzData.dzz_search)
        self.click_element(DzzLocator.dzz_search_result)

    # 点击党组织名称进入党组织详情页
    def dzz_details(self):
        time.sleep(2)
        self.click_element(DzzLocator.result_dzz_name)

from common.page_common import PageCommon
import time
from locator.Dzz.ldbz_locator import LdbzLocator


# 领导班子
class LdbzPage(PageCommon):
    # 点击领导班子Tab页
    def click_ldbz(self):
        self.click_element(LdbzLocator.ldbz_tab)
        time.sleep(2)

    # 新增换届信息
    def create_hjxx_btn(self):
        self.click_element(LdbzLocator.hjxx_create)
        time.sleep(2)

    # 新增换届信息
    def create_hjxx(self, **args):
        print(args['bzjs'])
        # self.input(LdbzLocator.hjxx_js, args['bzjs'])
        self.input(LdbzLocator.hjxx_js, 1)
        self.click_element(LdbzLocator.hjxx_rznx)
        self.click_element(LdbzLocator.rznx_1)
        self.click_element(LdbzLocator.hjxx_hjrq)
        self.click_element(LdbzLocator.hjrq_1)
        self.click_element(LdbzLocator.hjxx_hjxs)
        self.click_element(LdbzLocator.hjxs_1)
        time.sleep(3)
        self.click_element(LdbzLocator.qd_button)
        time.sleep(1)
        self.switch_to_alert()



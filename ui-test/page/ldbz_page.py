from common.page_common import PageCommon
import time
from locator.ldbz_locator import LdbzLocator


# 领导班子
class LdbzPage(PageCommon):
    # 点击领导班子Tab页
    def click_ldbz(self):
        self.click_element(LdbzLocator.ldbz_tab)
        time.sleep(2)

    # 新增换届信息
    def create_hjxx(self, **args):
        self.click_element(LdbzLocator.hjxx_create)
        time.sleep(2)
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
        time.sleep(3)
        # text = None
        # bl = False
        # if self.isElementPresent(By.XPATH, LdbzLocator.hjxx_alert_p):
        #     bl = True
        # elif self.isElementPresent(By.XPATH, LdbzLocator.hjxx_alert_h2):
        #     bl = False
        #     self.click_element(LdbzLocator.qx_button)
        # if bl == True:
        #     text = self.find_element(By.XPATH, LdbzLocator.hjxx_alert_p).text
        # elif bl == False:
        #     text = self.find_element(By.XPATH, LdbzLocator.hjxx_alert_h2).text
        # print(text)
        # return text

    def delete_hjxx(self):
        self.click_element(LdbzLocator.hjxx_deleted)
        self.click_element(LdbzLocator.hjxx_deleted_confirm)
        time.sleep(1)
        p_delete_text = self.alert_text(LdbzLocator.hjxx_alert_p)
        print(p_delete_text)



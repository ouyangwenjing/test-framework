import time

from common.page_common import PageCommon
from data.login_data import LoginData
from locator.login_locator import LoginLocator


# 登录页面
class LoginPage(PageCommon):

    # 登录页
    def jump_to(self):
        self.driver.get(LoginData.url_test)

    # 清空输入框缓存
    def clear_user(self):
        self.clear(LoginLocator.username_input)
        self.clear(LoginLocator.password_input)

    # 登录
    def login(self, username, password, code):
        self.input(LoginLocator.username_input, username)
        self.input(LoginLocator.password_input, password)
        self.input(LoginLocator.code_input, code)
        self.click_element(LoginLocator.login_btn)
        time.sleep(3)






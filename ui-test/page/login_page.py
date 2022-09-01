import time

from common.page_common import PageCommon
from data.login_data import LoginData
from locator.login_locator import LoginLocator


# 登录页面
class LoginPage(PageCommon):

    def jump_to(self):
        self.driver.get(LoginData.url)

    # 清空输入框缓存
    def clear_user(self):
        self.clear(LoginLocator.username_input)
        self.clear(LoginLocator.password_input)

    # 登录用户
    def login(self):
        self.input(LoginLocator.username_input, LoginData.username)
        self.input(LoginLocator.password_input, LoginData.password)
        self.input(LoginLocator.code_input, LoginData.code)
        time.sleep(3)
        self.click_element(LoginLocator.login_btn)






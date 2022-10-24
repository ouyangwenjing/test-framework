import time

from selenium.webdriver.common.by import By

from common.page_common import PageCommon
from data.login_data import LoginData
from locator.login_locator import LoginLocator


# 登录页面
class LoginPage(PageCommon):

    def __int__(self):
        self.driver.get(LoginData.url_test)

    # 登录页
    def jump_to(self):
        self.driver.get(LoginData.url_test)

    # 登录成功
    def login_success(self, username, password, code):
        self.input(LoginLocator.username_input, username)
        self.input(LoginLocator.password_input, password)
        self.input(LoginLocator.code_input, code)
        self.click_element(LoginLocator.login_btn)
        time.sleep(3)
        indexurl = self.get_current_url()
        return indexurl

    # 登录失败
    def login_error(self, username, password, code):
        self.input(LoginLocator.username_input, username)
        self.input(LoginLocator.password_input, password)
        self.input(LoginLocator.code_input, code)
        self.click_element(LoginLocator.login_btn)
        time.sleep(3)
        err_text = self.find_element(By.XPATH, LoginLocator.err_alert).text
        return err_text

    # 登录_手机号为空
    def login_Without_username(self, password, code):
        self.input(LoginLocator.password_input, password)
        self.input(LoginLocator.code_input, code)
        self.click_element(LoginLocator.login_btn)
        time.sleep(3)
        required_text = self.find_element(By.XPATH, LoginLocator.required_text).text
        return required_text

    # 登录_密码为空
    def login_Without_password(self, username, code):
        self.input(LoginLocator.username_input, username)
        self.input(LoginLocator.code_input, code)
        self.click_element(LoginLocator.login_btn)
        time.sleep(3)
        required_text = self.find_element(By.XPATH, LoginLocator.required_text).text
        return required_text

        # 登录_验证码为空
    def login_Without_code(self, username, password):
        self.input(LoginLocator.username_input, username)
        self.input(LoginLocator.password_input, password)
        self.click_element(LoginLocator.login_btn)
        time.sleep(3)
        required_text = self.find_element(By.XPATH, LoginLocator.required_text).text
        return required_text





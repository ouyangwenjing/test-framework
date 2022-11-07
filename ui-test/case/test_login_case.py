import time
import unittest

import ddt
import paramunittest
import os
from BeautifulReport import BeautifulReport

from base.assembler import Assembler
from page.login_page import LoginPage
from util.config_reader import config
from util.handle_excel_tool import HandleExcelTool
from util.log_tool import start_info, end_info, log
from util.screenshot_tool import ScreenshotTool


# 参数化构建参数
@paramunittest.parametrized(
    # 参数{语言，环境}
    {"lan": config['project']["lan"], "env": config['project']["env"]}
)
# 登录流程用例测试
@ddt.ddt
class TestLoginCase(unittest.TestCase):

    # 读取测试case
    xl_dir = os.path.dirname(os.path.dirname(__file__)) + '/data/test_login.xlsx'
    # 读取登录成功case
    login_suc_excel = HandleExcelTool(xl_dir, 'login_success')
    login_suc_cases = login_suc_excel.read_data()
    # 读取登录校验失败case
    login_error_excel = HandleExcelTool(xl_dir, 'login_error')
    login_error_cases = login_error_excel.read_data()
    # 读取登录必填项校验失败case
    login_required_excel = HandleExcelTool(xl_dir, 'login_required_item')
    login_required_cases = login_required_excel.read_data()
    print(login_suc_cases, login_error_cases, login_required_cases)

    # 出错需要截图时此方法自动被调用
    def save_img(self, img_name):
        ScreenshotTool().save_img(self.driver, img_name)

    # 参数化构建方法
    def setParameters(self, lan, env):
        self.lan = lan
        self.env = env

    # @BeforeTest
    def setUp(self):
        # 开始的 log 信息
        start_info()
        # 装配器初始化
        self.assembler = Assembler()

        # 提取驱动
        self.driver = self.assembler.get_driver()

        # 提取 mysql 工具
        self.mysql_tool = self.assembler.get_mysql()

        # 从 mysql 工具中拿到一个连接
        self.mysql_conn = self.mysql_tool.get_mysql_conn()
        sql = "SELECT username,mobile,party_org_id FROM system_users WHERE tenant_id  = '1'"
        log().info(self.mysql_tool.execute(sql))

    # @AfterTest
    def tearDown(self):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        self.assembler.disassemble_all()

    # 登录成功测试
    @unittest.skip
    @ddt.data(*login_suc_cases)
    @ddt.unpack
    @BeautifulReport.add_test_img(ScreenshotTool().get_img_name("test_1_TestLoginSuccessCase"))
    def test_1_TestLoginSuccessCase(self, xh, sjhm, mm, yzm):
        # print(xh, sjhm, mm, yzm)
        # 初始化登录页面
        login_page = LoginPage(self.driver)
        # 开启登录首页
        login_page.jump_to()
        # 输入账号密码登录
        index_url = login_page.login_success(sjhm, mm, yzm)
        # 登录成功断言
        try:
            self.assertEqual(index_url, "http://nginx.test.tyyd.com:8000/index")
            print("登录成功，正确跳转到主页面" + index_url)
        except AssertionError as msg:
            print("没有跳转到正确页面，当前跳转的地址为" + index_url + "\n报错信息如下" + format(msg))
            '''当断言失败时会抛出异常测试用例执行失败,输出提示信息后重新将异常抛出，即raise，
            若不重新抛出，用例则永远是显示执行成功的，因为它把异常处理掉了'''
            raise msg

        # # 强行截图
        # ScreenshotTool().save_img(self.driver, "force_test_1_TestLoginSuccessCase")

    # 错误手机号、密码、验证码登录测试
    @unittest.skip
    @ddt.data(*login_suc_cases)
    @ddt.unpack
    @BeautifulReport.add_test_img(ScreenshotTool().get_img_name("../../report/img/test_2_TestLoginErrorCase"))
    def test_2_TestLoginErrorCase(self, xh, sjhm, mm, yzm, expected):
        # print(xh, sjhm, mm, yzm, expected)
        # 初始化登录页面
        login_page = LoginPage(self.driver)
        # 开启登录首页
        login_page.jump_to()
        # 输入账号密码登录
        err_text = login_page.login_error(sjhm, mm, yzm)
        # 登录失败断言
        try:
            self.assertEqual(err_text, expected)
            print("登录失败断言成功，登录失败原因为" + expected)
        except AssertionError as msg:
            print("错误提示语与预期结果不一致，请检查" + err_text + "\n报错信息如下" + format(msg))
            '''当断言失败时会抛出异常测试用例执行失败,输出提示信息后重新将异常抛出，即raise，
            若不重新抛出，用例则永远是显示执行成功的，因为它把异常处理掉了'''
            raise msg

    # 手机号、密码、验证码为空登录测试
    @ddt.data(*login_required_cases)
    @ddt.unpack
    @BeautifulReport.add_test_img(ScreenshotTool().get_img_name("../../report/img"
                                                                "/test_3_TestLoginRequiredCase"))
    def test_3_TestLoginRequiredCase(self, xh, sjhm, mm, yzm, expected):
        # print(xh, sjhm, mm, yzm, expected, type(sjhm))
        # 初始化登录页面
        login_page = LoginPage(self.driver)
        # 开启登录首页
        login_page.jump_to()
        # 未输入必填项
        if sjhm is None:
            required_text = login_page.login_Without_username(mm, yzm)
        elif mm is None:
            required_text = login_page.login_Without_password(sjhm, yzm)
        elif yzm is None:
            required_text = login_page.login_Without_code(sjhm, mm)
        # 登录失败断言
        try:
            self.assertEqual(required_text, expected)
            print("登录失败,断言成功，登录失败原因为" + expected)
        except AssertionError as msg:
            # 强行截图
            # ScreenshotTool().save_img(self.driver, "TestLoginCase_0_test_3_TestLoginRequiredCase")
            print("错误提示语与预期结果不一致，请检查" + required_text + "\n报错信息如下" + format(msg))
            '''当断言失败时会抛出异常测试用例执行失败,输出提示信息后重新将异常抛出，即raise，
            若不重新抛出，用例则永远是显示执行成功的，因为它把异常处理掉了'''
            raise msg


# 当前用例程序入口
if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)

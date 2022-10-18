
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
    excel = HandleExcelTool(xl_dir, 'login')
    login_cases = excel.read_data()
    print(login_cases)

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

    # 登录测试
    @ddt.data(*login_cases)
    @ddt.unpack
    @BeautifulReport.add_test_img(ScreenshotTool().get_img_name("../../report/img/force_test_1_TestLoginCase"))
    def test_1_TestLoginCase(self, xh, sjhm, mm, yzm):
        print(xh, sjhm, mm, yzm)
        # 初始化登录页面
        login_page = LoginPage(self.driver)
        # 开启登录首页
        login_page.jump_to()
        # 清空输入缓存
        login_page.clear_user()
        # 输入账号密码登录
        login_page.login(sjhm, mm, yzm)

        # # 强行截图
        # ScreenshotTool().save_img(self.driver, "force_test_1_TestLoginCase")


# 当前用例程序入口
if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)

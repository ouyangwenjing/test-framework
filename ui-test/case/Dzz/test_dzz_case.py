
import time
import unittest
import paramunittest
import threading
from BeautifulReport import BeautifulReport
from page.Dzz.dzz_page import DzzPage
from page.Dzz.ldbz_page import LdbzPage
from util.config_reader import config
from util.log_tool import start_info, end_info
from util.screenshot_tool import ScreenshotTool
from util.thread_local_storage import ThreadLocalStorage


# 参数化构建参数
@paramunittest.parametrized(
    # 参数{语言，环境}
    {"lan": config['project']["lan"], "env": config['project']["env"]}
)
# 党组织用例测试
class TestDzzCase(unittest.TestCase):
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
        # 获取装配器对象
        self.assembler = ThreadLocalStorage.get(threading.current_thread())
        # 提取驱动
        self.driver = self.assembler.get_driver()

    # # @AfterTest
    # def tearDown(self):
    #     # 结束的 log 信息
    #     end_info()
    #
    #     # 装配器卸载
    #     self.assembler.disassemble_all()

    # 第一个测试点
    @BeautifulReport.add_test_img(ScreenshotTool().get_img_name("../../report/img/force_test_1_TestDzzCase"))
    def test_1_TestDzzCase(self):
        # 初始化首页
        dzz_page = DzzPage(self.driver)
        # 获取党组织管理页面
        dzz_page.click_dzz()
        # 搜索党组织
        dzz_page.search_dzz()
        # 党组织详情页
        dzz_page.dzz_details()
        # 休眠 5 秒方便观察页面运行效果
        time.sleep(0.5)


# 当前用例程序入口
if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)

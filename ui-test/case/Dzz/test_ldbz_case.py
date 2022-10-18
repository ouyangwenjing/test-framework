import os
import time
import unittest
import ddt
import paramunittest
import threading
from BeautifulReport import BeautifulReport
from page.Dzz.ldbz_page import LdbzPage
from util.config_reader import config
from util.log_tool import start_info, end_info
from util.screenshot_tool import ScreenshotTool
from util.thread_local_storage import ThreadLocalStorage
from util.handle_excel_tool import HandleExcelTool


@ddt.ddt
# 党组织用例测试
class TestLdbzCase(unittest.TestCase):
    # 读取测试case
    xl_dir =os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/test_create_ldbz.xlsx'
    excel = HandleExcelTool(xl_dir, 'Sheet1')
    cases = excel.read_data()

    # 出错需要截图时此方法自动被调用
    def save_img(self, img_name):
        ScreenshotTool().save_img(self.driver, img_name)

    # 参数化构建方法
    def setParameters(self, lan, env):
        self.lan = lan
        self.env = env

    @classmethod
    def setUpClass(cls):
        # 开始的 log 信息
        start_info()
        # 获取装配器对象
        cls.assembler = ThreadLocalStorage.get(threading.current_thread())
        # 提取驱动
        cls.driver = cls.assembler.get_driver()
        # 初始化领导班子Tab页
        cls.ldbz_page = LdbzPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        cls.assembler.disassemble_all()

    # 进入领导班子tab页
    def test_1_TestLdbzCase(self):
        # 进入领导班子tab页
        self.ldbz_page.click_ldbz()
        # 休眠 5 秒方便观察页面运行效果
        time.sleep(2)

    # 新增换届信息
    @ddt.data(*cases)
    def test_2_TestLdbzCase(self, case):
        time.sleep(2)
        # 提取测试数据
        params = eval(case['data'])
        title = case['title']
        expected = case['expected']
        print(params, type(params), title, type(title), expected, type(expected))
        # 调用新增换届方法
        self.ldbz_page.create_hjxx(**params)

    # 删除换届信息
    def test_3_TestLdbzCase(self):
        time.sleep(3)
        # 删除换届信息
        self.ldbz_page.delete_hjxx()
        time.sleep(5)


# 当前用例程序入口
if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=0)

import os
import unittest
from case import test_login_case
from case.Dzz import test_dzz_case,test_ldbz_case
from util.config_reader import config
from util.report_tool import ReportTool

# 报告存放路径
report_path = os.path.abspath(os.path.dirname(__file__))[
              :os.path.abspath(os.path.dirname(__file__)).find("test-framework") + len(
                  "test-framework")] + "/ui-test" + config['html']['htmlfile_path']
# 报告名字
report_name = config['html']["htmlfile_name"]

# 运行所有用例（单线程）
if __name__ == "__main__":
    # 创建测试套
    suites = unittest.TestSuite()
    loader = unittest.TestLoader()

    suites.addTests(loader.loadTestsFromModule(test_login_case))
    suites.addTests(loader.loadTestsFromModule(test_dzz_case))
    suites.addTests(loader.loadTestsFromModule(test_ldbz_case))

    # 报告生成器，运行用例并生成报告，对 BeautifulReport 套了一层外壳
    ReportTool(suites).run(filename=report_name, description='demo', report_dir=report_path, theme="theme_cyan")

import json
import os
import openpyxl


class HandleExcelTool:
    def __init__(self, filename, sheetname):
        """
        :param filename:excel文件名
        :param sheetname:表名
        """
        self.filename = filename
        self.sheetname = sheetname

    def read_data(self):
        # 根据文件名读取excel
        workbook = openpyxl.load_workbook(self.filename)
        # 读取表
        sheet = workbook[self.sheetname]
        res = list(sheet.rows)
        # 获取第一行表头
        title = [i.value for i in res[0]]
        # 遍历第一行之外的其他行
        cases = []
        for item in res[1:]:
            data = [i.value for i in item]
            dic = dict(zip(title, data))
            cases.append(dic)
        # 返回读出来的数据
        return cases


if __name__ == '__main__':
    xl_dir = os.path.dirname(os.path.dirname(__file__))+'/data/test_create_ldbz.xlsx'
    print(xl_dir)
    he = HandleExcelTool(xl_dir, 'Sheet1')
    print(he.read_data())
    case = he.read_data()
    print(type(he.read_data()))
    expected = eval(case[0]['data'])
    bzjs = expected['bzjs']
    print(bzjs, type(bzjs))
    print(expected, type(expected))


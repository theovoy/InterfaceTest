import json

import xlrd

class ExcelHandle:
    def read_excel_data(self, excel_path, sheet_name=None):
        """
        读取excel中的数据
        :param excel_path: excel路径
        :param sheet_name: 页签名称，默认第一个
        :return: 列表
        """
        wbook = xlrd.open_workbook(excel_path)
        wsheet = wbook.sheet_by_name(sheet_name)
        row = wsheet.nrows
        result = []
        for i in range(1,row):
            row_values = wsheet.row_values(i)
            #print(type(row_values))
            #data = json.loads(row_values)
            #print(data)
            result.append(row_values)
        return result
if __name__ == "__main__":
     handle=ExcelHandle()
     print(handle.read_excel_data('D:\\case.xlsx','Sheet1'))

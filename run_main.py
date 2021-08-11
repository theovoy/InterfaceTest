import time ,sys
# 引用模块路径
sys.path.append('./testcase')
sys.path.append('./db_fixture')
from common.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './testcase'
# 自动获取interface 目录下的测试用例
testsuit = defaultTestLoader.discover(test_dir,pattern='*test.py')


if __name__ == '__main__':
    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定制报告名称
    filename = './report/' + now + '_result.html'
    # 向报告写入测试结果数据
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试报告',
                            description='运行环境：环境：windows 10 浏览器：chrome 语言： Python3')
    # 运行测试集
    runner.run(testsuit)
    # 关闭报告文件
    fp.close()

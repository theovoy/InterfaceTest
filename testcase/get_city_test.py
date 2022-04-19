import json
import unittest
import requests
import logger
import genToken
import time
import loadData
logge = logger.Log()
handle = loadData.ExcelHandle()
timestamp=str(int(round(time.time() * 1000)))
tokens=genToken.Token()
token=tokens.gettoken(timestamp)
data1={
       "timestamp" : timestamp,
       "token" : token
}

class GetDepartureCity(unittest.TestCase):
    ''' 获取出发城市 '''
    def setUp(self):
        logge.info("开始执行测试".center(60,'#'))
        self.data = handle.read_excel_data('D:\\case.xlsx','Sheet1')
        self.base_url = self.data[0][1]
        data2 = eval(self.data[0][3])
        data2.update(data1)
        self.payload = json.dumps(data2)
        self.headers = eval(self.data[0][4])
        self.expect = self.data[0][5]

    def tearDown(self):
        logge.info(("接口返回数据:%s"%self.result).center(60, '#'))
        print(self.result)
        logge.info("测试执行结束".center(60,'#'))

    def test_1_get_city_all_null(self):
        ''' 所有参数 '''
        r = requests.post(self.base_url, data=self.payload, headers=self.headers)
        print(self.payload)
        print(self.base_url)
        self.result = r.json()
        self.assertEqual(self.result['code'], "200")
        self.assertEqual(self.result['msg'], self.expect)

if __name__ == '__main__':
    unittest.main()

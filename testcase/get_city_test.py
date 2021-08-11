import unittest
import requests
import logger
import genToken
import time
logge = logger.Log()

class GetDepartureCity(unittest.TestCase):
    ''' 获取出发城市 '''
    def setUp(self):
        logge.info("开始执行测试".center(60,'#'))
        self.base_url = "https://ebk.17u.cn/cxyopenapi/distributor/city/startCity"

    def tearDown(self):
        logge.info(("接口返回数据:%s"%self.result).center(60, '#'))
        print(self.result)
        logge.info("测试执行结束".center(60,'#'))

    def test_1_get_city_all_null(self):
        ''' 所有参数为空 '''
        payload = {"data": {"keyword": ""}, "channel":"" , "timestamp":"" , "token":"", "vcode": ""}
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.base_url, json=payload, headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], "401")
        self.assertEqual(self.result['msg'], '没有权限')

    def test_2_get_city_all(self):
        ''' 获取所有出发城市 '''
        timestamp=str(int(round(time.time() * 1000)))
        token=genToken.Token()
        payload = {"data": {"keyword": ""}, "channel":555 , "timestamp":timestamp , "token": token.gettoken(timestamp), "vcode": "TC007"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.base_url, json=payload, headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], "200")
        self.assertEqual(self.result['msg'], '获取成功')


if __name__ == '__main__':
    unittest.main()

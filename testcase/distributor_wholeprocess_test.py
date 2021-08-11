import unittest
import requests
import logger
import genToken
import time
logge = logger.Log()
timestamp=str(int(round(time.time() * 1000)))
token=genToken.Token()
class GetDepartureCity(unittest.TestCase):

    ''' 获取出发城市 '''
    def setUp(self):
        logge.info("开始执行测试".center(60,'#'))


    def tearDown(self):
        logge.info("测试执行结束".center(60,'#'))

    def test_1_get_city(self):
        ''' 查询出发城市 '''
        self.base_url = "https://ebk.17u.cn/cxyopenapi/distributor/city/startCity"
        payload = {"data": {"keyword": ""}, "channel":555 , "timestamp":timestamp , "token": token.gettoken(timestamp), "vcode": "TC007"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.base_url, json=payload, headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], "200")
        self.assertEqual(self.result['msg'], '获取成功')
        cityid= self.result['data']['cityList'][1]['cityId']

        ''' 到达城市查询 '''
        self.base_url = "https://ebk.17u.cn/cxyopenapi/distributor/city/endCity"
        payload = {"data": {"keyword": "","startCityId":cityid ,"startStationId": ""},"channel": 555,"timestamp": timestamp,"token": token.gettoken(timestamp),"vcode": "TC007"}
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.base_url, json=payload, headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], "200")
        self.assertEqual(self.result['msg'], '获取成功')

if __name__ == '__main__':
    unittest.main()

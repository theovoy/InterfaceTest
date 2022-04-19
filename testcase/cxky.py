#!/usr/bin/python
# -*- coding:utf8 -*-
import json
import jpype
import os
import time
import random
import requests
import genToken
# 创单


def order_pay():
    # data = {
    #     "endStation": "0",
    #     "equipmentSerialNo": "00000289",
    #     "lineId": 11111111,
    #     "lineName": "1路",
    #     "orderPrice": 0.01,
    #     "payPrice": 0.01,
    #     "ridingCodeContent": "${ridingCodeContentqa}",
    #     "startStation": "0",
    #     "startingTime": "${startingTime}",
    #     "thirdPartyOrderNo": "${thirdPartyOrderNo}",
    #     "vehicleNo": "京A2252"
    # }
    # str2 = {
    #     "timestamp": "timestamp",
    #     "token": "token",
    #     "vcode": "TEST001"
    # }
    # data = data + str2

    # 引入的jar包路径
    jar_path_gentoken = os.path.join(os.path.abspath('.'),
                                     r'E:\first\PycharmProjects\TicketMachine\cityTrans\genToken2\genToken.jar')
    jar_path_bcprov = os.path.join(os.path.abspath('.'),
                                   r'E:\first\PycharmProjects\TicketMachine\cityTrans\genToken2\bcprov-jdk15on-1.58.jar')
    jar_path_commons = os.path.join(os.path.abspath('.'),
                                    r'E:\first\PycharmProjects\TicketMachine\cityTrans\genToken2\commons-lang3-3.3.2.jar')
    jar_path_commons2 = os.path.join(os.path.abspath('.'),
                                     r'E:\first\PycharmProjects\TicketMachine\cityTrans\genToken2\commons-lang-2.6.jar')
    # jre路径jvm.dll
    jvmPath_32 = r"E:\second\Pycharm\PyCharm 2018.3.5\jre64\bin\server\jvm.dll"
    # 启动虚拟机
    #jpype.startJVM(jpype.getDefaultJVMPath(), '-Djava.class.path=%s;%s;%s;%s' % (jar_path_gentoken, jar_path_bcprov, jar_path_commons, jar_path_commons2))
    #JPackage = jpype.JPackage('com.ly.traffic.ground.saas.distributor')  # 包和类
    timestamp = int(round(time.time() * 1000))  # 时间戳毫秒
    print("timestamp:", timestamp)
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 日期时间
    # print("datetime:", datetime_s)
    # 【预发-临沂】【预发-临沂】【预发-临沂】【预发-临沂】
    # vcode = "SD001"
    # secret = "f6b4e228683c428a94fc705aedd8b64c"
    # ridingcode = "FXIQpD6C19PyYb62zvp4GOEwjv4G8WRc6kMK1N6oG00QCuYWFBp+oHPo+XZkxohw7siKp4rFPLc1BtMjgQk1RETHfmLqzHdZps" \
    #              "/j40jX55s="
    #【预发-同程旅行测试专用-会员卡】【预发-同程旅行测试专用-会员卡】
    # vcode = "TC007"
    # secret = "59ba9e20ed84445281ae9c116a265878"
    # ridingcode = "uI4pYX2hnEGnOX7pwU87DeEwjv4G8WRc6kMK1N6oG02CiN9z/gDvgN+p6/06LoNQZ6D7v7mJn2/2nQmmPacgXRneYrCsFvE7quJF6z3idUw="
    #[预发-江阴城镇公交][预发-江阴城镇公交][预发-江阴城镇公交]--有效
    # vcode = "JS001"
    # secret = "ddbb7ba8bb344469b741e20566d9d720"
    #    ridingcode = "ve1/uhfGGh8wUVkG5SqmXOEwjv4G8WRc6kMK1N6oG02uN0EWZeJPenupFyOmrasTAGhLPWnVlhOYiHBaEau8dETHfmLqzHdZps/j40jX55s="

    #玉芬-临沂
    #    vcode = "SD001"
    #    secret = "f6b4e228683c428a94fc705aedd8b64c"
    #    ridingcode='tI632vU00WLmwfqDuFWN7ZBmOXW9DvvDY7hwa0SdkIjWzyqRs7eT1ZZU9e5zR5479TxBPxoMnmDiF47Z204SQQ=='
    #    ridingcode ="mTXsTrf8T+/1YDfX0pz7Sjaj+Qk7Qy4NWQ1hOvi1KbzljieLg1ap9Z1iYqmfOvT3NplK/bwSjgqKtfk1vWNg9w=="
    #    ridingcode="FXIQpD6C19PyYb62zvp4GOEwjv4G8WRc6kMK1N6oG01exBJ6qWeK8tXCagaE9F/99TxBPxoMnmDiF47Z204SQQ=="
    #【皖美出行】
    #【城乡测试】
    vcode ="cxkytest"
    secret ="568360e6e48947b7bcf65b3183820423"
    ridingcode="1124130" #乐趣
    #ridingcode="F9Q9ymv0wBXESq9yH0NO1xdPo0rCmQgvW4zROUNjJ3S+T4cKsv8cOr5shBgrDhMVIp/9WQywx7I8GpPTfQo0HA==" #自己
    #ridingcode=""#乐趣

    orderPrice = payPrice =1
    #j_token = JPackage.TokenGen.initToken(timestamp, secret, vcode)  # 生成token 预发环境-临沂
    # j_token = JPackage.TokenGen.initToken(1606377886128, "c799905523fb49c293b8b896b0007b97", "SD001")  # 生成token
    #token = str(j_token)
    token=genToken.Token().gettoken(str(timestamp))
    print("token值:", token)
    #    token_s = '\"' + token + '\"'
    #    print("token值:", token_s)
   # jpype.shutdownJVM()  # 关闭虚拟机
    no = random.randint(1, 10000000000000000000000000)
    print("orderNo:", no)
    data = {
        "data": {
            "endStation": "0",
            "equipmentSerialNo": "00000289",
            "lineId": 11111111,
            "lineName": "预发1路",
            "orderPrice": orderPrice,
            "payPrice": payPrice,
            "ridingCodeContent": ridingcode,
            "startStation": "0",
            "startingTime": datetime,
            "thirdPartyOrderNo": no,
            "vehicleNo": "测A0008",
            "companyName": "pre test 有限公司"
        },
        "timestamp": timestamp,
        "token": token,
        "vcode": vcode
    }
    print("data:", data)
    status_code, text = post(data)
    print("status_code,text:", status_code, text)


def post(data) -> object:
    site = 'http://tcmobileapi.t.17usoft.com'  # 预发环境
    url = site + '/urptopenapi/orderinfoapi/order/pay'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers, timeout=1)
        return response.status_code, response.text
    except Exception as e:
        #        self.logger.error("Time out!")
        print("Time out!")
        return None

order_pay()


'''
if __name__ == '__main__':
    p = Pay()
    p.post()
'''
#    print(status_code)
#    print(text)

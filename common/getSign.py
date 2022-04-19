import hashlib, json
class Sign:
    def getsign(self,key):

       json1='{\"cardNo\":\"TC00700000122\",\"openId\":\"oFg_y0Hlw0uJa_u5wdBTfc6am-9c\",\"orderPrice\":\"14\",\"passengerNum\":\"1\",\"shiftScheduleId\":\"94098306\",\"startTime\":\"2022-03-25 23:03\",\"thirdPartyOrderNo\":\"SB121\",\"ticketInfoList\":[{\"ticketTypeId\":\"30\",\"ticketTypeName\":\"成人票\",\"ticketNum\":\"1\"}],\"ticketMachineNo\":\"JSS11249\",\"vcode\":\"TC007\"}'
       #json1="{\"vcode\":\"TC001\",\"cardNo\":\"00000721\",\"shiftScheduleId\":\"109781\",\"openId\":\"oFg_y0Hlw0uJa_u5wdBTfc6am-9c\",\"passengerNum\":\"1\",\"orderPrice\":\"0.01\",\"startTime\":\"2021-12-28 23:00\",\"thirdPartyOrderNo\":\"SB121\",\"ticketMachineNo\":\"JSS11249\",\"ticketInfoList\":[{\"ticketTypeId\":\"27\",\"ticketTypeName\":\"成人票\",\"ticketNum\":\"1\"}]}"
       #data="{\"vcode\":\"TC007\",\"cardNo\":\"TC00100011481\",\"lineId\":\"27436\",\"online\":\"1\"}"
       #json1=json.dumps(data)
       json1 +=key
       print(json1)
       si=hashlib.md5(json1.encode('utf8')).hexdigest()
       print(json1.encode('utf8'))
       return si
if __name__ == "__main__":
    sign=Sign()
    eg=sign.getsign('2be575933da856b6a2ce311e706f3a82')
    print(eg)
import unittest
import get_city_test,get_endcity_test,distributor_wholeprocess_test,cancel_order_test,create_order_test
import HTMLTestRunner
import get_shift_detail_test,update_order_status_test
import get_shift_test
import qurey_order_test
from configEmail import SendEmail

testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(get_city_test.GetDepartureCity))
testunit.addTest(unittest.makeSuite(get_endcity_test.GetEndCity))
testunit.addTest(unittest.makeSuite(get_shift_test.GetShift))
testunit.addTest(unittest.makeSuite(get_shift_detail_test.GetShiftDetail))
testunit.addTest(unittest.makeSuite(create_order_test.CreateOrder))
testunit.addTest(unittest.makeSuite(update_order_status_test.UpdateOrderStatus))
testunit.addTest(unittest.makeSuite(qurey_order_test.QureyOrder))
testunit.addTest(unittest.makeSuite(cancel_order_test.CancelOrder))
testunit.addTest(unittest.makeSuite(distributor_wholeprocess_test.WholePrecess))
file=open("D:\\cxy\\InterfaceTest-main\\report\\result.html","wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=file,title=u"定制客运分销接口",description=u"测试结果")
runner.run(testunit)
m = SendEmail(
    username='529836597@qq.com',
    passwd='tofarepamtpsbich',
    recv=['peigang.qin@ly.com'],
    title='定制客运生产环境接口测试结果',
    content='测试结果',
    file=r'D:\cxy\InterfaceTest-main\report\result.html',
    ssl=True
)
m.send_email()
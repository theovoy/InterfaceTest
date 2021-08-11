import unittest
import get_city_test,get_endcity_test,distributor_wholeprocess_test
import HTMLTestRunner

testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(get_city_test.GetDepartureCity))
testunit.addTest(unittest.makeSuite(get_endcity_test.GetEndCity))
testunit.addTest(unittest.makeSuite(distributor_wholeprocess_test.GetDepartureCity))
file=open("D:\\cxy\\InterfaceTest_master-master\\report\\result.html","wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=file,title=u"定制客运分销接口",description=u"测试结果")
runner.run(testunit)
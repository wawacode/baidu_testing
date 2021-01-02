#导入单元测试框架
import unittest
from  selenium import webdriver
'''
以下是测试人员写的测试百度
1、测试百度搜入框的有效性
'''
#编写一个测试类
#TestCase是测试用例的意思
class TestBaidu(unittest.TestCase):
    #继承TestCase必须有的setUp用例启动的方法
    def setUp(self):
        #启动模拟浏览器
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
    #自己定义的一个测试方法,测试用例验证输入框有效性
    def test_input(self):
        #find_element_by_id利用id找元素
        so=self.driver.find_element_by_id("kw")
        #做断言,断言输入框的有效性 is_enabled（)表示是否有效
        self.assertTrue(so.is_enabled(),True)

    #继承TestCase必须有的tearDown用例结束的方法

    def tearDown(self):
        #退出浏览器
        self.driver.quit()
if __name__=="__main__":
    print("测试用例的执行")
    #定义unitest.TextTestRunner()对象
    test=unittest.TextTestRunner()
    #执行这个test_input测试用例，只能执行一个用例,
    test.run(TestBaidu("test_input"))


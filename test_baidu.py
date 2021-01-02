#导入单元测试框架
import unittest
from  selenium import webdriver
from utils.HTMLTestRunner_Chart import HTMLTestRunner
import time
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
        #需要做截图，需要创建一个图片列表，相当于截图列表,固定 imgs
        self.imgs=[]
    #自己定义的一个测试方法,测试用例验证输入框有效性
    def 测试百度搜索框有效性(self):
        #find_element_by_id利用id找元素
        so=self.driver.find_element_by_id("kw")
        #添加截图功能,self.driver.get_screenshot_as_base64是截图的编码
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #做断言,断言输入框的有效性 is_enabled（)表示是否有效
        self.assertTrue(so.is_enabled(),True)
    #定义一个新的测试用例，在输入框中输入中公教育，判断输入框中是否是“中公教育”值
    def 测试输入框输入中公教育有效性验证(self):
        #find_element_by_id利用id找输入框
        so = self.driver.find_element_by_id("kw")
        #传入数据send_keys
        so.send_keys("中公教育")
        #find_element_by_id找到"百度搜索"按钮,点击一下
        self.driver.find_element_by_id("su").click()
        #休眠一会:
        time.sleep(20)
        #抓图编码
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #验证输入框中的数据是否传入"中公教育",断言输入框内容就是中公教育
        #get_attribute取属性<input value=""/>
        self.assertEqual(so.get_attribute("value"),"中公")
    #继承TestCase必须有的tearDown用例结束的方法

    def tearDown(self):
        #退出浏览器
        self.driver.quit()
if __name__=="__main__":
    print("测试用例的执行")
    '''
    #定义unitest.TextTestRunner()对象
    test=unittest.TextTestRunner()
    #执行这个test_input测试用例，只能执行一个用例,
    test.run(TestBaidu("test_input"))
    '''
    #执行多个用例用TestSuite
    #实例一个TestSuite
    suit=unittest.TestSuite()
    #在TestSuite测试套件中加入"测试百度搜索框有效性"这个测试方法
    suit.addTest(TestBaidu("测试百度搜索框有效性"))
    #在套件中加入第二个测试用例
    suit.addTest(TestBaidu("测试输入框输入中公教育有效性验证"))
    #不在控制台输出，打印测试报告，测试报告是一个文件html文件
    with open("files/result5.html","wb") as f:
        '''
        HTMLTestRunner测试报告第一个参数文件f,
        verbosity=2测试报告的详细情况，
        title测试报告名称，
        description测试报告描述情况
        '''
        runner=HTMLTestRunner(f,verbosity=2,title="百度搜索框有效测试用例",description="对百度搜索框有效度进行测试")
        runner.run(suit)
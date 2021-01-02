#导入单元测试框架
import unittest
'''
这段是开发者写的加法实现类
'''
class User():
    def add(self,a,b):
        return a+b
'''
以下是测试人员写的测试上面方法的测试用例
'''
#编写一个测试类
#TestCase是测试用例的意思
class TestAdd(unittest.TestCase):
    #继承TestCase必须有的setUp用例启动的方法
    def setUp(self):
        print("测试用例的开始")
    #自己定义的一个测试方法,第一个测试用例实现3+4=7
    def test_add(self):
        user=User()
        #测试的目的是下断言，常用的断言是True或False
        #assertEqual第一个参数断言的结果，后面是函数的使用
        self.assertEqual(7,user.add(3,4))
    #自己定义的另一个测试方法,第二测试用例实现0.1+0.2=0.3
    def test_add_one(self):
        user=User()
        #断言：0.1+0.2=0.3
        self.assertEqual(0.3,user.add(0.1,0.2))
    #继承TestCase必须有的tearDown用例结束的方法
    def tearDown(self):
        print("测试用例的结束")
if __name__=="__main__":
    print("测试用例的执行")
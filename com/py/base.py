#coding=utf-8

# 类
class MyClass:
    name = "Hello"
    age = 20
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("name:" + MyClass.name + "-" + self.name)
        print("age:" + str(MyClass.age) + "-" + str(self.age))
        
    # 类方法
    @classmethod
    def classMethod(self, name):    
        print(self.name + name)
    
    # 静态方法
    @staticmethod
    def staticMethod(x, y):
        print(x + y)
        
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

# 函数，全局可调用
def say(name):
    print(name)

# 默认参数，注：默认参数一般放在最后
def sayHello(action, name="Hello"):
    print(action + "-" + name)

if __name__ == '__main__':
    say("Hello world.");
    sayHello("Hello.")
    sayHello("Hello.", "World.")
    
    m = MyClass("张三", 33)
    print(m.getName())
    print(m.getAge())

    MyClass.classMethod(".world");
    MyClass.staticMethod(4, 6)
    

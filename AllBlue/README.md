# 此代码为个人兴趣开发；AllBlue 根据项目取名
# Time：2019/08/25
# Creator：xhaoge,


# 项目简介；
main.py --> 实为整个程序的入口，定义一个总的class进入；
CommonFunc --> 定义公共所需部分，所有的类都将继承一个基类Base.py,
                将nightking的返回定义一个类进行数据统一处理，以及其他；
Handle  --> 定义控制各种测试用例的环境，进行数据准备；
Source  --> 定义数据来源，通过读取xml文件中的配置，提供各脚本所需数据；
TestCase --> 测试用例的集合；

# 规定：
测试脚本中使用 “—”的方式命名，在其他脚本中使用驼峰式命名，见名知意；


# 注意点：
基本配置xml文件，在AllBlue\Source\BasicConfig.xml下，须先熟知；
log收集位置，亦在xml文件中配置，没有文件夹就自动创建；



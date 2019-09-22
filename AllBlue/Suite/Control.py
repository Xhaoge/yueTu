# 定义在测试用力run前的数据处理；

import importlib
from AllBlue.TestCase.AllCaseBase import CaseBase

class Controler(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info('==============测试开始 =============')
        self.buildSearchCase()

    def buildSearchCase(self):
        self.runcase = ''
        for runner in self.caseList:
            print("Casename:"+runner["Casename"],"   Address:"+runner["Address"])
            try:
                caseModule = importlib.import_module(runner["Address"])
                ModuleClass = getattr(caseModule,runner["Casename"])
                self.caseRun = ModuleClass()
                self.caseRun.TestProcess()
                print('========================')
            except Exception as e:
                self.log.error('casename:%s,报错：%s'%(runner["Casename"],e))
            self.caseRun.TestResult()


    # todo 每运行一个测试脚本，会去读取一次配置待解决

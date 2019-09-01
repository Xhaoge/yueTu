# masterCurrency case
# 此case用于测试环境简单的测试几个平台请求，以及检查本位币的取值情况；
# iwoflyCOM/wogo请求币种是HKD,本位币是HKD,其他币种请求，本位币是USD;
# 其他平台无论什么请求币种，本位币都是CNY;


import json
from NewWorld.CommonFunc.NightKingResponse import NightKingRes
from NewWorld.TestCase.AllCaseBase import CaseBase

class Case_Search_KeyValue_0002(CaseBase):

    def __init__(self):
        CaseBase.__init__(self)
        self.log.info("Case_Search_KeyValue_0002,测试开始")


    def TestProcess(self):
        self.log.info('Case_Search_KeyValue_0002,进入测试步骤！')

        self.log.info('测试ctrip的本位币,请求币种是CNY,本位币应该是USD')
        self.Test_Master_Currency(plat='ctrip', reqC='CNY', MstCurrecy='CNY')

        self.log.info('测试iwofly的本位币,请求币种是CNY,本位币应该是USD')
        self.Test_Master_Currency(plat='iwoflyCOM', reqC='CNY', MstCurrecy='USD')

        self.log.info('测试iwofly的本位币,请求币种是USD,本位币应该是USD')
        self.Test_Master_Currency(plat='iwoflyCOM', reqC='CNY', MstCurrecy='USD')

        self.log.info('测试iwofly的本位币,请求币种是HKD,本位币应该是HKD')
        self.Test_Master_Currency(plat='iwoflyCOM', reqC='CNY', MstCurrecy='USD')

        self.log.info('测试iwoflyCN的本位币,请求币种是CNY,本位币应该是CNY')
        self.Test_Master_Currency(plat='iwoflyCN', reqC='CNY', MstCurrecy='CNY')


    def TestResult(self):
        self.log.info('Case_Search_KeyValue_0002,测试完毕')
        print("测试结果很成功，perfect！")


    def Test_Master_Currency(self,plat='ctrip',reqC='CNY',MstCurrecy='CNY'):
        self.nkRequestData['Cid'] = plat
        self.nkRequestData['Currency'] = reqC
        print(self.nkRequestData)
        self.sendData = json.dumps(self.nkRequestData)
        self.log.info(self.sendData)
        res = self.sendRequest(method='POST', url=self.nkRequesturl, data=self.sendData)
        if res:
            self.log.info('搜索成功，有返回')
            case2_nk = NightKingRes(res)
            ms_currency = case2_nk.routingFirstBaseInfo('masterCurrency')
            if ms_currency != MstCurrecy:
                self.log.error('%s 请求币种为 %s 时，mastercurrencty为：%s' % (plat,reqC,ms_currency))
            self.log.info('%s 请求币种为 %s 时，mastercurrencty为：%s' % (plat,reqC,ms_currency))
            print(case2_nk.nkRouting)
        else:
            self.log.error('搜索无返回，或者返回信息为null；')


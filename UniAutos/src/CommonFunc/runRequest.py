import requests
import json

# 定义一个基本请求类，后续有其他请求方式再逐步完善；

class RunRequest:

    def post_main(self,url,data,header=None):
          if header !=None:
             res = requests.post(url=url,data=data,headers=header)
          else:
             res = requests.post(url=url,data=data)
          return res.json()

    def get_main(self,url,data=None,header=None):
         if header !=None:
             res = requests.get(url=url,data=data,headers=header,verify=False)
         else:
             res = requests.get(url=url,data=data,verify=False)
         return res.json()

    def sendRequest(self,method,url,data=None,header=None):
         if method.upper() == 'POST':
             res = self.post_main(url,data,header)
         else:
             res = self.get_main(url,data,header)
         return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
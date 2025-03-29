import requests

class _AxiosPY:
    def __init__(self,request):
        self.axios:requests=request
    
    def Post(self,header={},data=None,url=None):
        response = self.axios.post(headers=header,data=data,url=url)
        return response
    
    def Get(self,header={},url=None):
        response = self.axios.get(headers=header,url=url)
        return response
    

Axios=_AxiosPY(requests)
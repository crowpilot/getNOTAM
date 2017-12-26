#ugokanai

import pycurl
import io
import certifi
import datetime

def aislogin():

    curl=pycurl.Curl()
    curl.setopt(pycurl.CAINFO,certifi.where())
    curl.setopt(pycurl.URL,"https://aisjapan.mlit.go.jp/LoginAction.do")
    curl.setopt(pycurl.POST,1)
    curl.setopt(pycurl.HTTPPOST,[('formName','ais-web'),('userID',''),('password','')])
    curl.setopt(pycurl.COOKIEJAR,'cookie.txt')
    
    curl.setopt(pycurl.SSL_VERIFYPEER,0)
    curl.setopt(pycurl.SSL_VERIFYHOST,0)
    
    curl.perform()
    return 

def getNotam():
    today=datetime.datetime.today()
    fromdate=today.strftime("%y%m%d0000")
    todate=(today+datetime.timedelta(days=7)).strftime("%y%m%d0000")
    
    curl=pycurl.Curl()
    curl.setopt(pycurl.CAINFO,certifi.where())
    curl.setopt(pycurl.URL,"https://aisjapan.mlit.go.jp/KeySearcherAction.do")
    curl.setopt(pycurl.COOKIEFILE,'cookie.txt')
    curl.setopt(pycurl.POST,1)
    curl.setopt(pycurl.HTTPPOST,[('location','RJNH'),
                                 ('period','0'),
                                 ('notamKbn','1'),
                                 ('firstFlg','true'),
                                 ('periodFrom',fromdate),
                                 ('periodTo',todate),
                                 ('dispScopeA','true'),
                                 ('dispScopeE','true'),
                                 ('dispScopeW','true')])
    
    curl.setopt(pycurl.SSL_VERIFYPEER,0)
    curl.setopt(pycurl.SSL_VERIFYHOST,0)
    
#    b=io.BytesIO()
#    curl.setopt(pycurl.WRITEFUNCTION,b.write)
    
    try:
        curl.perform()
 #       ret=b.getvalue()
#        http_code=curl.getinfo(pycurl.HTTP_CODE)
        
 #       f=open("notamdata","w")
#        f.write(ret)
#        f.close
        
        
    except Exception as e:
        ret=str(e)
        print "error"
        
#    return ret

if __name__ == '__main__':
    aislogin()
    getNotam()
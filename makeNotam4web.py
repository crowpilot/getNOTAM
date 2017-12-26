# -*- coding: utf-8 -*-
import io
import os
import urllib2
import re
import datetime
import shutil
from HTMLParser import HTMLParser

def login():
    return

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag=False
        self.notam=""
        self.lastdata=""
        self.codeCK=False
        self.code=""

    
    def handle_starttag(self,tag,attrs):
        if tag=='b':
            self.codeCK=True
            
        if tag=='td':
            attrs= dict(attrs)
            if 'class' in attrs:
                if 'txt-notam' in attrs['class']:
                    self.flag=True
                    self.notam=""

    def handle_data(self,data):
        if self.flag:
#            print data.split("   ")
            self.notam += str(data).replace("\r","").replace("\t","").replace("\n","").replace("　","").replace(" ","")+" "

        if self.codeCK:
            if data[0:2]=="RJ":
                self.code=data
            self.codeCK=False
#            print 'aaaaaaaaaaaaaaaaaaaaaaaa'


    def handle_endtag(self,tag):
        if tag=='td':
            self.flag=False
            print self.notam
            if re.match(" \d\d\d\d \d\d",self.notam):
#                print "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                f=open("notamdata/"+self.notam[1:5]+"-"+self.notam[6:8],"w")
                f.write(self.code+" "+self.notam[1:5]+"-"+self.notam[6:8]+" ")
                f.close()
                self.lastdata=self.notam[1:5]+"-"+self.notam[6:8]
                
            elif self.lastdata:
                f=open("notamdata/"+self.lastdata,"a")
                f.write(self.notam)
                f.close()
                
            self.notam=""


def parseData():
    file=os.listdir('./htmldata/')
    for name in file:
        f=open('htmldata/'+name,'r')
        parse=MyParser()
        parse.feed(f.read())


def checkData4w():
    file=os.listdir('./notamdata/')
    today = datetime.date.today().day
    rjnhtable="<h2>RJNH</h2><table border='1'>"
    rjngtable="<h3>RJNG</h3><table border='1'>"
    rjnatable="<h3>RJNA</h3><table border='1'>"
    rjnktable="<h4>RJNK</h4><table border='1'>"
    rjtjtable="<h4>RJTJ</h4><table border='1'>"
    for name in file:
        if name=="del" or name=="old":
            break
        print name
        f=open("notamdata/"+name,"r")
        line=f.read()
        data=line.split()
        AP=data[0]
        print data
        if AP=="RJNH":
            rjnhtable += '<tr><td><span style="color:black;font-size:20px">'+line+"</span></td></tr>"
        elif AP=="RJNG":
            rjngtable+='<tr><td><span style>'+line+'</span></td></tr>'
        elif AP=="RJNA":
            rjnatable+='<tr><td><span style>'+line+'</span></td></tr>'
#        print data[3]+" "+data[2][8:10]
        f.close()
    rjnhtable+="</table>"
    rjngtable+="</table>"
    rjnatable+="</table>"
    rjnktable+="</table>"
    rjtjtable+="</table>"
    
    nh=open("html/tables.html","w")
    nh.write(rjnhtable+rjngtable+rjnatable+rjnktable+rjtjtable)
    nh.close()
    
if __name__=='__main__':
#    login()
    parseData()
    checkData4w()

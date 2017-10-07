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
    file=os.listdir('/home/pi/getNOTAM/htmldata/')
    for name in file:
        f=open('htmldata/'+name,'r')
        parse=MyParser()
        parse.feed(f.read())



def checkData():
    file=os.listdir('/home/pi/getNOTAM/notamdata/')
    today = datetime.date.today().day
    for name in file:
        if name=="del" or name=="old":
            break
        print name
        f=open("notamdata/"+name,"r")
        data=f.read().split()
        fromd=data[3]
        tod=data[5]
        title=data[1]
#        print data[3]+" "+data[2][8:10]

        if int(fromd[6:8])-today+2:
            if fromd[3:8]==tod[3:8]:
                print title+" ck"
                if int(fromd[8:10])>11 and int(fromd[8:10])<21 and int(tod[8:10])>11 and int(tod[8:10])<21:
                    print "delete(night)"
                    print fromd[6:8]
                    shutil.move('notamdata/'+name,'notamdata/del/'+name)
                else:
                    print "not remove"
            else:
                print title+" continue"
        else:
            print title+" delete(old)"
        f.close()
    
if __name__=='__main__':
#    login()
    parseData()
    checkData()

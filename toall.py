# -*- coding: utf-8 -*-

import os

fullcontent=""
for i in os.listdir("./"):
    if i.find(".txt")!=-1:
        f=open(i)
        content=f.read()
        fullcontent=fullcontent+content

fw=open("all.txt","w")
fw.write(fullcontent)
fw.flush()
fw.close()
﻿from striprtf.striprtf import rtf_to_text
import json
import os
dirname = './descript/'


def getRft(filename):
    fileName= dirname+filename
    with open(fileName) as infile:
        content = infile.read()
        text = rtf_to_text(content)
        return(text)
    # print(text)


if __name__ == '__main__':
    files = os.listdir(dirname)
    # print(files)
    aList=[]    
    for file in files:
        rtf= getRft(file)
        # print(rtf)    
        splitted_text = str(rtf).split()
        s={}
        s['name']=splitted_text[0]
        s['file']=file
        aList.append(s)

    
    
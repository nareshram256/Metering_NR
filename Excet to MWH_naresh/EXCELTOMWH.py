from glob import glob
import os
import time
import os.path
import csv
from os import path
import xlsxwriter 
import numpy as np
import random
import pandas as pd
import re
from datetime import datetime,timedelta, date
import numpy as np # linear algebra




#from google.colab import files

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if (filename in dir):
            result.append(os.path.join(root,filename))
        #if filename in files:
           # result.append(os.path.join(root, filename))
    return result[0]


def do_print(meter,new_p,k):  
    wright=[]
    if(path.exists(new_p+"\\" + meter +'.MWH')):
        f=open(new_p+"\\" + meter +'.MWH', 'r')
        line=f.readlines() 
        for i in range (1,25):
            for q in range (0,4):
                dd=(float(line[i][10+18*q:20+18*q]))*(-1)
                wright.append(dd)
        print("Meter %s data added for the date %s "%(meter,k))
    else:
        print('\n No data exists in the %s folder %s'%(meter,k))
    return  wright


def exceldata_MW(main,d,ppp,noo,tobereplacedmeterno):  
   
    #noo=input("enter no of days data needed: ")
    #d   = input('Enter starting date format ddmmyy: ')
    new_p='null'
    workbook = xlsxwriter.Workbook('met_data'+'.xlsx')
    worksheet = workbook.add_worksheet('M and S data')
    dtt=['00:00:00','00:15:00','00:30:00','00:45:00','01:00:00','01:15:00','01:30:00','01:45:00','02:00:00','02:15:00','02:30:00','02:45:00','03:00:00','03:15:00','03:30:00','03:45:00','04:00:00','04:15:00','04:30:00','04:45:00','05:00:00','05:15:00','05:30:00','05:45:00','06:00:00','06:15:00','06:30:00','06:45:00','07:00:00','07:15:00','07:30:00','07:45:00','08:00:00','08:15:00','08:30:00','08:45:00','09:00:00','09:15:00','09:30:00','09:45:00','10:00:00','10:15:00','10:30:00','10:45:00','11:00:00','11:15:00','11:30:00','11:45:00','12:00:00','12:15:00','12:30:00','12:45:00','13:00:00','13:15:00','13:30:00','13:45:00','14:00:00','14:15:00','14:30:00','14:45:00','15:00:00','15:15:00','15:30:00','15:45:00','16:00:00','16:15:00','16:30:00','16:45:00','17:00:00','17:15:00','17:30:00','17:45:00','18:00:00','18:15:00','18:30:00','18:45:00','19:00:00','19:15:00','19:30:00','19:45:00','20:00:00','20:15:00','20:30:00','20:45:00','21:00:00','21:15:00','21:30:00','21:45:00','22:00:00','22:15:00','22:30:00','22:45:00','23:00:00','23:15:00','23:30:00','23:45:00']

    date_formats = ('dd/mm/yy hh:mm:ss')
    date_format = workbook.add_format({'num_format': date_formats,'align': 'left'})
    worksheet.write(0, 0,"Date")  
    worksheet.write(0, 1,"Block")
    #date_1 = datetime.strptime(d, "%d%m%y")
    date_1 = datetime.strptime(d.replace('\n',''), "%d%m%y")
    for j in range (int(noo)):
        end_date = date_1 + timedelta(days=j)
        k=end_date.strftime("%d")+end_date.strftime("%m")+end_date.strftime("%y")

        for r in range (96*j,96+96*j):
            worksheet.write(r+1, 0,k[0:2]+"-"+k[2:4]+"-"+"20"+k[4:6])
            date_time = datetime.strptime(k[0:2]+"-"+k[2:4]+"-"+"2020"+" " +dtt[(r%96)],'%d-%m-%Y %H:%M:%S')
            worksheet.write(r+1,1,date_time,date_format)
            #worksheet.write(r+1,1,)  
    for u in range (1):
        col=u+2
        #row=1
        worksheet.write(0, col,main)
        date_1 = datetime.strptime(d.replace('\n',''), "%d%m%y")
        for j in range (int(noo)):
            end_date = date_1+ timedelta(days=j)
            k=end_date.strftime("%d")+end_date.strftime("%m")+end_date.strftime("%y")
            if(main!='0'):
                new_p=find_files(k,ppp)
            data_new=do_print(main,new_p,k)
            for i in range (0,(len(data_new))):
                worksheet.write(96*j+i+1, col,data_new[i])


    workbook.close()   

    time.sleep(3)
    dfs = pd.read_excel("met_data.xlsx" ,sheet_name='M and S data')
    return data_replaced(dfs,d,noo,tobereplacedmeterno)




def data_replaced(d,nn):
    
    dtt=['0000','0100','0200','0300','0400','0500','0600','0700','0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200','2300']
    date_1 = datetime.strptime(d.replace('\n',''), "%d%m%y")
    dfs = pd.read_excel("met_data.xlsx" ,sheet_name='M and S data')
    for head in dfs.columns[2:,]:
        tobereplacedmeterno=head
        gpno=input("Enter req group no needed UX-XX ") 
        for n in range (int(nn)):
            K=dfs[head][0+96*n:96+96*n].values
            end_date = date_1 + timedelta(days=n)
            k1=end_date.strftime("%d")+end_date.strftime("%m")+end_date.strftime("%y")


            createFolder('./'+k1+'/')
            l2=open(k1+'/'+tobereplacedmeterno+'.MWH','w') 
            l2.write(gpno+" "+ tobereplacedmeterno[0:2]+'-'+tobereplacedmeterno[2:6]+'-'+tobereplacedmeterno[6:]+"   "+k1[0:2]+'-'+k1[2:4]+'-'+k1[4:6]+"    "+"-2139.2002     1882.2      0.0")
            l2.write('\n')
            s=0
            for i in range (24):
                l2.write(dtt[i])
                l2.write('      ')
                for j in range (4):
                    a=K[s]
                    a=format(a, '.6f')
                    if('-' in str(a) and len((str(int(K[s])))) >2):
                        l2.write(str(a))
                        l2.write('        ')

                    elif('-' in str(a) and len((str(int(K[s]))))==2):
                        l2.write(' ')
                        l2.write(str(a))
                        l2.write('        ')
                    elif(len((str(int(K[s]))))==1):
                        if('-' in str(a)):
                            l2.write(' ')
                            l2.write(str(a))
                            l2.write('        ') 
                        else:    
                            l2.write('  ')
                            l2.write(str(a))
                            l2.write('        ')
                    elif(len((str(int(K[s]))))==2):
                        l2.write(' ')
                        l2.write(str(a))
                        l2.write('        ') 
                    elif(len((str(int(K[s]))))==1):
                        l2.write('   ')
                        l2.write(str(a))
                        l2.write('        ')          
                    else:
                        #l2.write(' ')
                        l2.write(str(a))
                        l2.write('        ')    
                    s=s+1
                l2.write('\n')   
            l2.close()
    return       


if __name__ == '__main__':
     noo=input(" no of days to be replaced: ")
     d=input("Enter start date ddmmyy: ")
     #ppp="C:\\SEMbase\\"
     ppp='data\\'
     ss=input("Do u have excel Y: N")
     if(ss=='N' or ss=='n'):
        WRONG_METER=input("Enter the required meter no name of the format NPxxxxb ")
        CORRECT_METER=input("Enter corret meter no npxxxb: ")
        exceldata_MW(CORRECT_METER,d,ppp,noo,WRONG_METER)
     else:
         
         data_replaced(d,noo)   
     #dfs = pd.read_excel("met_data.xlsx" ,sheet_name='M and S data')
     #data_replaced(dfs,d,int(noo),tobereplacedmeterno)
     #dfs = pd.read_excel('bawna diplapur1.xlsx', name=['date','value'])
     print("Sucess")
     time.sleep(2)
from glob import glob
import time
from datetime import datetime,timedelta, date
from magic_append import *
from n_nrx import nrx
from abruptreadings import *
from n_comb_mrg import *
import pandas as pd
from meter_notin_master import *
from To_ERWR import *
#import numpy as np
#from google.colab import files

def runfoldercorrect():
    sre=input(" Do u have srea file ? Y/N ")
    fp = input('Enter filename ddmm: ')
    if(sre=='N' or sre=='n'):
       print('append start') 
       magic_app(fp)
    f=open('NPC_data//'+fp +'srea'+'.npc', 'r')
    line=f.readlines()
    STOP=[]
    fp1 = input('Enter stop(mon) date dd-mm-yy: ')
    date_1 = datetime.strptime(fp1, "%d-%m-%y")
    for i in range (5):
        end_date = date_1 + timedelta(days=i)
        d=end_date.strftime("%d")+"-"+end_date.strftime("%m")+"-"+end_date.strftime("%y")
        STOP.append(d)
        
        
    STOP1=[]    
    for i in range (7):
        end_date = date_1 - timedelta(days=i+1)
        d=end_date.strftime("%d")+"-"+end_date.strftime("%m")+"-"+end_date.strftime("%y")
        STOP1.append(d)    
    #fp1 = input('Enter stop date1 dd-mm-yy: ')
    #STOP1=fp1
    #fp2 = input('Enter stop date2 dd-mm-yy: ')
    #STOP2=fp2
    #fp3 = input('Enter stop date3 dd-mm-yy: ')
    #STOP3=fp3
    #fp3 = input('Enter stop date4 dd-mm-yy: ')
    #3STOP4=fp3
    #fp3 = input('Enter stop date5 dd-mm-yy: ')
    # code to extract columns in meaningful manner from Master file (Mapping file between Location ID and Meter Number)
    def master(patth):
        import csv
        import pandas as pd
        import xlsxwriter

        data=[]
        with open(patth+'MASTER.DAT') as csvfile:							# loading data from master mapping file
            readtxt=csv.reader(csvfile,delimiter=" ")				# every field splitted on the basis of {space}. Hence single spaces have been removed
            for row in readtxt:										# taking data into list
                data.append(row)
                
        x=len(data)
        #print(x)
        z=x
        x=x-6													# useless data adjustment
        #data.remove(data[1])
        data.remove(data[1])

        #print(data[0])

        i=0
        while i<x:
            j=0
            while j<len(data[i]):
                if data[i][j].endswith('\t'):						# to only remove tab spaces at end of string not the strings that are merged within
                    data[i][j] = data[i][j].replace("\t", "")		# removing tab spaces finding \t substring and replacing it with 
                elif '\t' in data[i][j]:
                    z=data[i][j].split('\t')
                    #print(z[0])
                    #print(z[1])
                    p=j+1
                    data[i][j]=z[0]
                    data[i].insert(p,z[1])

                j=j+1
            # print(data[i])
            i=i+1


        i=0															


        while i<x:
            j=0
            while j<len(data[i]):
                if len(data[i][j])==0: 								# condition to remove null string
                    data[i].remove(data[i][j])						# removing null strings from list
                    j=j-1											# program logic
                j=j+1
            #print(data[i])
            i=i+1


        data.remove(data[-1])
        data.remove(data[-1])
        data.remove(data[-1])
        data.remove(data[-1])
        data.remove(data[-1])
        data.remove(data[-1])


        i=0
        x=len(data)
        while i<x:
            j=5
            string=""
            while(j<len(data[i])):
                string=string+" "+data[i][j]
                data[i][j]=""
                j=j+1
            data[i][5]=string
            i=i+1




        i=0
        while i<len(data):
            if ' at ' in data[i][5]:
                s=data[i][5].split(' at ')
                data[i][5]=s[0]
                x=1
                while x<len(s):
                    data[i][6]=data[i][6]+s[x]
                    x=x+1
            elif ' AT ' in data[i][5]:
                s=data[i][5].split(' AT ')
                data[i][5]=s[0]
                x=1
                while x<len(s):
                    data[i][6]=data[i][6]+s[x]
                    x=x+1
            m=data[i][1]
            m=m[-1]
            data[i][7]=m
            i=i+1


        data[0][6]='STATION'
        data[0][7]='TYPE'

        for row in data:
            print(row)


        with xlsxwriter.Workbook('NPC_data\\Master.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, data in enumerate(data):
                worksheet.write_row(row_num, 0, data)
        return 



    #STOP5=fp3
    rr=[]
    new1=[]
    with open('NPC_data/'+fp + 'n_extra_meters' + '.txt','w') as mm:
        with open('NPC_data/'+fp + 'naresh' + '.npc','w') as off:
    
            #L2=open(r'C:\SEMPro\MASTER.DAT','r')
            master('C:\\SEMPro\\')
            typ_gp1=pd.read_excel('NPC_data\\Master.xlsx')
            #line2=L2.readlines()[2:]
            lst=[]
            #for i in range (0,len(line2)):
            #    for j in range (30):
            #        if('-A' in line2[i][j:j+2] or '-B' in line2[i][j:j+2] and 'M - MAIN METER' not in line2[i] and  'S - STANDBY METER' not in line2[i] and  'C - CHECK METER' not in line2[i] and 'L - LOSSES METER' not in line2[i]):
            #            lst.append(line2[i][j-7:j+2])
            for i in typ_gp1[typ_gp1.columns[1]].values:
                lst.append(i)
           
          
            #lst=['NP-6018-B','NP-6017-B','NP-6113-A','NP-5074-A','NP-9981-A','NP-5274-A','NP-5273-A','NP-7684-A','NP-8634-A','NP-8647-A','NP-8648-A','NP-8649-A','NP-8650-A','ER-1195-A','ER-1192-A','ER-1473-A', 'ER-1474-A','ER-1074-A','ER-1075-A', 'NP-7841-A','NP-6062-A','NP-7867-A','NP-7868-A','NP-6061-A', 'NP-6065-A', 'NP-6093-A','NP-6092-A','NP-7411-A','NP-7410-A','ER-1217-A', 'ER-1218-A','NP-6091-A', 'NP-6514-A','NP-6515-A','NP-8699-A', 'NP-7412-A','NP-6513-A','NP-6516-A','ER-1318-A','NP-8633-A','NP-8658-A','NP-8659-A']
            for j in range (0,len(lst)):
                for i in range(0, len(line)):
                    if (('WEEK FROM 0000 HRS OF' in line[i]) and (STOP[0] in line[i][::-1][0:9][::-1] or STOP[1] in line[i][::-1][0:9][::-1] or STOP[2] in line[i][::-1][0:9][::-1] or STOP[3] in line[i][::-1][0:9][::-1] or STOP[4] in line[i][::-1][0:9][::-1])):
                        
                        if(((lst[j] in line[i+1]) or (lst[j] in line[i+2])) and (lst[j] not in rr)):
                            rr.append(lst[j])
                            new1.append(line[i+1])
                            new1.append(line[i+2])
                            print('\n The meter added',lst[j])
                            for k in range(0,25*11):
                                if(k==0):
                                    off.write(line[i+k])                                         
                                if(k>0 and ((i+k)< len(line))):   
                                    if(('WEEK FROM' not in line[i+k]) and ('--' not in line[i+k]) and ('ÄÄÄÄÄ' not in line[i+k])):
                                        off.write(line[i+k])     

                                    else:
                                        break                       
            
            
            print('\n Total meters added=',len(rr))
            my_df1 = pd.DataFrame(rr) 
            my_df1.to_csv('NPC_data/'+fp+'lst_mtrs.csv',header=['METER'])
            pp=[]
            for j in range (0,len(lst)):
                for i in range(0, len(line)):
                    if (('WEEK FROM 0000 HRS OF' in line[i]) and (STOP1[0] in line[i][::-1][0:9][::-1] or STOP1[1] in line[i][::-1][0:9][::-1] or STOP1[2] in line[i][::-1][0:9][::-1] or STOP1[3] in line[i][::-1][0:9][::-1] or STOP1[4] in line[i][::-1][0:9][::-1] or STOP1[5] in line[i][::-1][0:9][::-1] or STOP1[6] in line[i][::-1][0:9][::-1])):

                        if(((lst[j] in line[i+1]) or (lst[j] in line[i+2])) and (lst[j] not in rr)):
                            rr.append(lst[j])
                            new1.append(line[i+1])
                            new1.append(line[i+2])
                            print('\n The partial meter added',lst[j])
                            mm.write('\n The partial meter added  '+lst[j] +" " +line[i])

                            pp.append(lst[j])
                            for k in range(0,25*11):
                                if(k==0):
                                    off.write(line[i+k]) 
                                if(k>0 and ((i+k)< len(line))):   
                                    if(('WEEK FROM' not in line[i+k]) and ('--' not in line[i+k]) and ('ÄÄÄÄÄ' not in line[i+k])):
                                        off.write(line[i+k])     

                                    else:
                                        break          
            
            my_df3=pd.DataFrame(pp)  
            my_df3.to_csv('NPC_data/'+fp+'p_lst_mtrs.csv',header=['METER'])  
        new1=np.asarray(new1)
        f=open('NPC_data//'+fp +'srea'+'.npc', 'r')
        line=f.readlines()
        print('\n Total  meters added inclusive partial data=',len(rr))
        print('\n Total meters in masters data=', len(lst))
        print("\n Total meters inside master= ", len(new1))
        nrx.nrx(fp,fp1)
        #oth = open('NPC_data/'+fp + 'meter_not_in MAster' + '.txt','w')
        #off2=open('NPC_data/'+fp+"MeterNAM"+'.NPC','w')
        #for i in range(0, len(line)):
        #        if (('WEEK FROM 0000 HRS OF' in line[i]) and (STOP[0] in line[i] or STOP[1] in line[i] or STOP[2] in line[i] or STOP[3] in line[i] or STOP[4] in line[i])):
        #            count=0
        #            for sss in range (len(new1)):
        #                if(line[i+1][0:8] in new1[sss]):
        #                    count+=1
        #            if(count==0):
        #                print("Meter not in Master",line[i+1])
        #                oth.write(line[i+1])
        #                for k in range(0,25*11):
        #                    if(k==0):
        #                        off2.write(line[i+k])                                         
        #                    if(k>0 and ((i+k)< len(line))):   
        #                        if(('WEEK FROM' not in line[i+k]) and ('--' not in line[i+k]) and ('ÄÄÄÄÄ' not in line[i+k])):
        #                            off2.write(line[i+k])     

        #                        else:
        #                            break   
        #oth.close()
        #off2.close()
            
    zerofinding(fp)
    runirdata(fp)
    meter_notin_master(fp)
    #to_erwr(fp)
    return 
runfoldercorrect()
    
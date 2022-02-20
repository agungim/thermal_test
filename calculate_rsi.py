import csv
import sys
import datetime

txtname1=str(sys.argv[0])
txtname2=str(sys.argv[0])

print(txtname1)
print(txtname2)
with open("Data_heatflux_hut3.txt",'r') as contain1: 
    arr1=contain1.readlines()                                                                                         
    #arr1 = csv.reader(contain1)
    del arr1[0]

with open("Data_thermocouple_hut3.txt", 'r') as contain2:  
    arr2=contain2.readlines()                                                                                        
    #arr2 = csv.reader(contain2)g
    del arr2[0]

arr=[]
lastvalue=0
for n,line1 in enumerate(arr1):
    #print('cek0')
    if n==0:
        spl1=line1.split("\t")
        datetime10=float(spl1[0])        
        continue
    spl1=line1.split("\t")
    datetime11=datetime10
    datetime10=float(spl1[0])
    for m,line2 in enumerate(arr2):
        spl2=line2.split("\t")
        datetime2=float(spl2[0])
        if datetime2>datetime11 and datetime2<=datetime10:
            #print('cek1')
            
            add1=str(datetime10)
            for i in range(len(spl1)):
                if i<1:continue
                if spl1[i].strip()=='':continue
                add1=add1+','+spl1[i]
            add1=add1+','+str(datetime2)
            for i in range(len(spl2)):
                if i<1:continue
                if spl2[i].strip()=='':continue
                add1=add1+','+spl2[i]
            dt=datetime2-lastvalue    
            add1=add1+','+str(dt)                    
            arr.append(add1)
            lastvalue=datetime2
            break

print(arr)
with open(txtname1+'_1.csv', "w") as textfile:
    for element in arr:
        textfile.write(element + "\n")  
        


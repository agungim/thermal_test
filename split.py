import sys

csvname=str(sys.argv[1])

csvfile = open(csvname, 'r').readlines()
filename = 1
eachline=10000000
lastdate=0.0
plus=0
for i in range(len(csvfile)):
    if i==0:
        spl=csvfile[i].split(",")
        print(spl[0])
        lastdate=float(spl[0])
        plus=0 

    if i % eachline == 0:
        arr=[]
        for j in range(eachline):
            if i+j+1 > len(csvfile):break
            spl=csvfile[i+j].split(",")
            #ind=str(plus+int(spl[0]))
            if lastdate>float(spl[0]):
                plus=plus+lastdate
                
            ind=plus+float(spl[0])    
            if j % 100 ==0:
                str=spl[0]+','+format(ind, '.2f')
                for n in range(len(spl)):
                    if n<1:continue
                    str=str+','+spl[n]
                lastdate=float(spl[0])   
                arr.append(str)
            lastdate=float(spl[0])    

        #open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+100000])
        open(csvname+'_'+format(filename, '.0f') + '.csv', 'w+').writelines(arr)
        filename += 1
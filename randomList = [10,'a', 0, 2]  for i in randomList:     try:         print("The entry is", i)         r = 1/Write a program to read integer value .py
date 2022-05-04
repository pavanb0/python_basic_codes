fn=input('Enter File Name with extension:')
try:
    f=open(fn,'r')
    sum=0
    for data in f:
        sum=sum+int(data)
except FileNotFoundError:
    print('Wrong File name Entered')
except ValueError:
    print('File containing a non-int element')
else:
    print('Sum of all numbers:=',sum)
    f.close()

input()

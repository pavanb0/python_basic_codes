 try:
    sum=0
    for i in range(5):
        n=int(input('Enter Even number:'))
        if n%2!=0:
            raise Exception( "Enter only Even Number")
        else:
            sum=sum+n
except Exception as e:
    print(e)
else:        
    print('Sum:',sum)
input()


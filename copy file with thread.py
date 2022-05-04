import threading
se=open("C:\\Users\\a2z\\Videos\\21FCS023_15_PAVAN_BAGWE.pdf","rb")
new=open("C:\\Users\\a2z\\Desktop\\fuck.pdf","wb")
def thr():
    new.write(se.read())
thr=threading.Thread(target=thr)
thr.start()
se.close()
new.close()

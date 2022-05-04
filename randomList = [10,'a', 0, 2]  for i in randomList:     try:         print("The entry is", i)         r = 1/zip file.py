from zipfile import *
f = ZipFile('d:\\test.zip', 'w', ZIP_DEFLATED)
f.write('d:\\myfile.txt')
f.write('d:\\myfile1.txt')
f.write('d:\\myfile2.txt')
print('test.zip file created...')
f.close()

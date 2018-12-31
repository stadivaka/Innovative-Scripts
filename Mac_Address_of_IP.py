import os,re
r=input('ip\n\r')
os.system('ping '+r+' > info.txt')
os.system("arp -a "+r+" > info.txt")
file=open('info.txt','r+')
data=file.read()
X = '([a-fA-F0-9]{2}[:|\-]?){6}'
a = re.compile(X).search(data)
if a:
    print (data[a.start(): a.end()])

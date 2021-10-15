import json
def r2j(o):
	return json.loads(o[o.find('(')+1:-1])
import os
import requests as rs
params={}
params['callback']='jQuery1122020434276543850394_1593947609770'
s='http://tacc.radio.cn/pcpages/searchs'
params['searchType']=3
params['offset']=1
params['limit']=20
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
def su(k):
	params['keyWord']=k
	html=rs.get(s,params=params,headers=headers)
	j=r2j(html.text)
	id=[]
	for a in j['data']:
		id.append(a['id'])
	return id	
	

def exist_value():
	li=[a for a in os.walk('.')]
	con=''
	for a in li:
		for b in a[2]:
			con+=b+'\n'
	ll=con.split('\n')
	#con=[]
	#for a in ll:
	#	if '.m4a' in a:
	#		con.append(a)
	#exists=ll
	return ll
	#return con
#ll=exist_value()
#print(exist_value())
#for a in ll:
#	print(a)
#	print('a[0]:'+a[0]+'  ____ a[-1]:'+a[-1])
#exit()

def du(id,page,rows=100):
	return r2j(rs.get('http://tacc.radio.cn/pcpages/odchannelpages?callback=jQuery112204192831370651957_1593991296342&od_id={0}&start={1}&rows={2}'.format(id,page,rows),headers=headers).text)['data']['program']

import glob
import _thread as qd
nums=0	
import time

lists=[]
names=[]
#exists=None
def download(id,rpath,num=0):
	#global exists
	exists=exist_value()
	#print('current work folder :' +os.getcwd())
	#input()
	path=os.getcwd()
	try:
		os.chdir(rpath)
	except:
		os.mkdir(rpath)
		os.chdir(rpath)
	#exists=glob.glob('*')
	'''
	li=[a for a in os.walk('.')]
	con=''
	for a in li:
		for b in a[2]:
			con+=b+'\n'
	ll=con.split('\n')
	exists=ll
	'''
	page=1
	global lists, names
	global nums
	nums=0	
	while True:
		j=du(id,page)
		if j==[]:
			print('list search complete')
			print('Please wait for download process')
			break
		#try:
		#	url=j[0]['streams'][1]['url']
		#except:
			#print('url == NULL' )
			#break
		#url=j[0]['streams'][0]['url']
		for a in j:
			name=a['onlinetime']+' '+a['name']+'.m4a'
			if name in exists:
				#print(name +' in exists')
				#exit()
				continue
			#else:
			  	#print(name.encode('utf-8'))
			  	#print(name+' not in exists')
			  	#print('the length of name is ' + str(len(name)))

				#exit()
		
			url=a['streams'][1]['url']
			lists.append(url)
			if url=='':
				#print(a['streams'])
				print('  '+name+' not normal quality audio, use big size instead')
				lists.pop(-1)
				lists.append(a['streams'][0]['url'])
			names.append(name)
		if num :
			lists=lists[:num]
		#print('len(lists)='+str(len(lists)))
		while len(lists):
			nums+=1
			qd.start_new(down,(lists.pop(0),names.pop(0)))
				
			#while nums>=10:
			while nums>=5:
				#print('I am waiting ')
				#print('I am ',nums)
				#time.sleep(10)
				time.sleep(1)
		if num!=0:
			break;
		page+=1	
	#print('nums ='+str(nums))	
	while nums:
		#time.sleep(10)
		time.sleep(1)
	os.chdir(path)

record={}
def down(u,name):
	global lists,names,nums,record
	#print(u)
	
	try:
		#html=rs.get(u,timeout=40)
		print(u)
		html=rs.get(u,stream=True)
		#html=rs.get(u)
	except:
		'''
		if name in record:
			record[name]+=1
		else:
			record[name]=1
			
		if record[name]<3: 
		'''
		lists.append(u)
		names.append(name)
		print(name," round again")
		print(u)
		nums-=1
		return
	
	'''
	#print('curl '+u+' -o "'+name+'"')
	if u=='':
		print("u=''")
	elif u==None:
		print('u==None')
	'''
	'''
	if u!='':
	#	return
		os.system('curl '+u+' --user-agent "'+headers['User-Agent']+'" -o "'+name+'"')
	nums-=1
	return 
	'''
	#os.system('sleep 100')
	name_down=name+'.downloading'
	#name_down=name
	f=open(name_down,"wb")
	#f.write(html.content)
	#f.close()
   # num=0
	for a in html.iter_content(chunk_size=1024*1024):
		if a:
			f.write(a)
	#		num+=1
	if f.tell()== int(html.headers['Content-Length']):
		print('\t',name, ' check pass')
	else:
		f.close()
		print('\t\t',name, ' check fail')
		lists.append(u)
		names.append(name)
		print(name," round again")
		print(u)
		nums-=1
		return



	f.close()
   # if num>=80:
   #	 os.rename(name_down,name)
   # else:
	   # os.remove(name_down)
	   # print(name_down+'less than 80 M')

	os.rename(name_down,name)
	print(name+" --{}M-- download complete".format(int (os.stat(name).st_size/1024/1024)))
	nums-=1
	return 


def less_than(byte):
	#global exists
	exists=glob.glob('*.m4a')
	#exists=exist_value()
	sum=[]
	for a in exists:
		t=os.stat(a)
		if t.st_size <byte:
			sum.append(a)
	return sum		


def del_list(l):
	for a in l:
		os.remove(a)


			



				



import yt
import thousands_go as go
if __name__ =='__main__':
	name=r'李峙的不老歌'
	#li=yt.su('李峙的不老歌')
	li=yt.su(name)
	#yt.download(li[0],rpath=r'李峙的不老歌',num=1)
	#yt.download(li[0],rpath=name,num=1)
	yt.download(li[0],rpath=name)
	#yt.download(li[0],rpath=r'李峙的不老歌')
	go.go(name)






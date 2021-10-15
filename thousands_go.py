import os
import glob

def year_month_day(name):
	a=name.split('-')
	return (a[0],a[1],a[2].split(' ')[0])

def mkdir(name):
	try:
		os.mkdir(name)
	except:
		pass
import shutil
def go(name):
	#os.chdir('千里共良宵')
	#os.chdir('李峙的不老歌')
	os.chdir(name)
	li=glob.glob('*.m4a')
#import os

	for a in li:
		if '-' in a:
			try:
				b=year_month_day(a)
			except:
				continue
			mkdir(b[0])
			mkdir(b[0]+'/'+b[1])
			#os.system('mv "'+a+'" '+b[0]+'/'+b[1])
			shutil.move(a, b[0]+'/'+b[1])



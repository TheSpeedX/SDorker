import sys
import urllib
import progressbar
def main():
	vul=[]
	fi=open(sys.argv[1],"r")
	st=fi.read()
	fi.close()
	link=st.split("\n")
	i=1
	with progressbar.ProgressBar(max_value=len(link)) as bar:
		for s in link:
			try:
				if s:
					response=urllib.urlopen(s+"%27")
					res=response.read()
					if "error" in res:
						vul.append(s)
					bar.update(i)
					i=i+1
			except:
				i=i+1
	print str(len(vul))+" Websites Found Vulnerable"
	f2=open("SDSQLi.txt","w")
	for v in vul:
		print v
		f2.write(v+"\n")
	f2.close()
	print "\nSite List Saved With Filename: SDSQLi.txt"
if __name__=="__main__":
	main()

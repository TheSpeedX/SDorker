import sys,urllib
def main():
	f=open(sys.argv[1],"r")
	str=f.read()
	f.close()
	p=str.split("<a href=")
	for s in p:
		if s.lower().find("url?q=") == 2:
			stin=8
			ein=int(s.find("&amp;"))
			t=s[stin:ein]
			t=urllib.unquote_plus(t)
			print t
if __name__=="__main__":
	main()

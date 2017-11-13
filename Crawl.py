# @author Anshuman
# Basic Crawler
import urllib.request
import timeit
import webbrowser
def findurls( html,count):
    for look in html:
        if "<a href=" in look and "http://" in look:
            start=look.find("http://")
            end=look.find("\"",start)
            urllist.append(look[start:end])
            print(count)
            print("\t")
    maxpage=500
    while len(urllist)< maxpage and count < len(urllist)-1:
        try:
            local_filename1, headers1 = urllib.request.urlretrieve(urllist[count])
            count+=1
            html1=open(local_filename1,encoding="utf8")     
            findurls(html1,count)
            print(count)
            print("\n")
        except:
            break
        
urllist=[]
start=timeit.default_timer()
local_filename, headers = urllib.request.urlretrieve('https://python.org/')
html = open(local_filename,encoding="utf8")
count=0
findurls (html,count);
stop=timeit.default_timer()
urllist=list(set(urllist))
print (urllist)
print (len(urllist))
print (stop-start)

    

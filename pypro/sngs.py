import urllib.request
import urllib.parse
import re
import urllib
import wget
import os


os.system('clear')
os.system('cls')

print ('''\t\t\t Select A mode  
[1] Download from direct entry
Press any other key from keyboard to exit''')
AskAQuestion = input(">>>")

if  AskAQuestion == '1':

	song = input("Enter the song name: ")


        try:
		query_string = urllib.parse.urlencode({"search_query" : song})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	except:
		print("Network Error")
		quit()


	DownloadLinkOnly = "http://www.youtubeinmp3.com/fetch/?video="+"http://www.youtube.com/watch?v=" + search_results[0]
	try:
		filename = wget.download(DownloadLinkOnly)        # download the song in working directory	
	except:
		print('Error..!!')

else:
	print("\nExiting.......")

print("\nHave a good day.")

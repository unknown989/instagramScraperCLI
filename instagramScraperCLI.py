import requests
from bs4 import BeautifulSoup as bs
import json
import sys
import random
import string
import os

def main(user):
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"}
	r = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query="+user,headers=headers).json()
	user = r["users"][0]["user"]["username"]
	r = requests.get("https://www.instagram.com/"+user,headers=headers)
	sp = bs(r.text,"html.parser")
	body = sp.find("body")
	data = body.find("script",text=lambda t:t.startswith("window._sharedData"))
	data = str(data).replace('<script type="text/javascript">window._sharedData = ',"")
	data = str(data).replace(";</script>","")

	data = json.loads(data)

	images = []


	preloadimages = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
	
	for i in preloadimages:
		try:
			img = i["node"]["display_url"]
			images.append(img)
		except:
			pass

	return images


try:
	filename = sys.argv[1]
except:
	sys.exit("No file is entered")


with open(filename,"r") as f:
	list_ = f.read()

list_ = list_.split("\n")
list_ = [i.lower() for i in list_]
list_ = list(set(list_))

try:
	os.mkdir("./Accounts")
	print("Accounts/ is created")
except:
	print("Accounts/ Already there")


for index,i in enumerate(list_):
	try:
		images = main(i)
		dirc = os.getcwd()+"/Accounts/"+i
		os.mkdir(dirc)
		for ind,o in enumerate(images):
			sys.stdout.write("\r{} {}/{} : {}/{}".format(str(i),str(len(list_)),str(index+1),str(ind+1),str(len(images))))
			sys.stdout.flush()
			r = requests.get(o).content
			fn = "".join(random.choices(string.ascii_letters+string.digits,k=8))+".jpg"
			with open(dirc+"/"+fn,'wb') as f:
				f.write(r)
	except Exception as e:
		print(e)
		
	print("\n")

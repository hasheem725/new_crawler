from django.shortcuts import render
from django.http import HttpResponse

import re
import ast
import requests

url = "http://edition.cnn.com"

# Create your views here.

def crawler():
	data = {}
	source_code = requests.get(url)
	plain_text = source_code.text
	source_string = re.findall('{\"articleList\":.*?}]}',plain_text,re.I)
	souce_code_dict = ast.literal_eval(source_string[0])
	count = 1
	for article in souce_code_dict['articleList']:
		if re.search('trump',article['description'],re.I):
			print("Article " + str(count) + " " + article['description'])
			print("URI " + article['uri'])
			data[article['headline']] = []
			data[article['headline']].append(url + article['uri'])
			data[article['headline']].append(article['description'])
	return data

def index(request):
	header = "<html><head><title>CNN Crawler</title></head>"
	body = "<body style=\"background-color:#33daff\"><font color='#ff33ff'><center><div><h1 style=\"text-shadow:2px 2px 5px #ff33ff\">Trump & Clinton All the latest updates<h1></div></center></font>"
	data = crawler()
	links = "<div style=\"width:600\">"
	for line in data:
		links = links + "<div><p style=\"max-width:2px,word-wrap:break-word\"><a href='%s' target='_blank'>%s</a></p><p>%s</p></div>"%(data[line][0],line,data[line][1])
	links = links+"</div>"
	link2 = "<div style=\"display:inline-block,vertical-align:middle,float:right,align-content:center,display:flex\"><p>Hello Hasheem</p></div>"		
	return HttpResponse(header + body + links + link2 +"</body></html>")
	#return render(request,'spider/home.html')
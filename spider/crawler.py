import re
import ast
import requests

url = "http://edition.cnn.com"

def crawler():
	source_code = requests.get(url)
	plain_text = source_code.text
	source_string = re.findall('{\"articleList\":.*?}]}',plain_text,re.I)
	souce_code_dict = ast.literal_eval(source_string[0])
	count = 1
	for article in souce_code_dict['articleList']:
		if re.search('trump',article['description'],re.I):
			print("Article " + str(count) + " " + article['description'])
			print("URI " + article['uri'])

crawler()
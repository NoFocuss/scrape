from bs4 import *
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disabling the warning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
 

# Initial URL PROMPT-----Returns User URL
def init_prompt():
	user_url = input('Please enter a valid URL for a website that you would like to scrape:\n')
	return user_url


# RETURNS REQUEST(GLOBAL)
def req(the_url):
	url = the_url
	try:
		r = requests.get(str(url), verify=False)
	except: 
		print("Something went wrong. Please try another URL")
		req()
	return requests.get(str(url), verify=False)


# which data to return from req
def datareq_prompt():
	user_req = input('What type of data would you like to see? \nOptions: \n\'text\'\n\'content\'\n\'raw\'\n\'json\'\n')
	return user_req


# RUN THE ROGRAM
def run():
	url = init_prompt()
    # define request
	r = req(url)

	r.status_code

	if str(r.status_code) == '200':
		print('Connection Successful!')
		print('Encoding: '+r.encoding)
	else:
		print('Something went wrong')


	# MAKE SOUP
	page = BeautifulSoup(r.content, 'html.parser')
	final = page.encode('utf-8')
	print(final)
	print(page.prettify)	
	

# Program Start Below
print('Welcome to the scraper!')
run()